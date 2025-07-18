import streamlit as st
import streamlit.components.v1 as components
st.set_page_config(layout="wide")
custom_html = """
<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Investment Case Table</title>
    <script src='https://cdnjs.cloudflare.com/ajax/libs/xlsx/0.18.5/xlsx.full.min.js'></script>
    <script src='https://cdn.jsdelivr.net/npm/handsontable@11.1.0/dist/handsontable.full.min.js'></script>
    <link rel='stylesheet' href='https://cdn.jsdelivr.net/npm/handsontable@11.1.0/dist/handsontable.full.min.css'>
    <style>
        body {
            font-family: 'Segoe UI', Arial, sans-serif;
            background: #f7f7fa;
            margin: 0;
        }
        .main-wrap {
            max-width: 1200px;
            margin: 32px auto 0 auto;
            background: #fff;
            border-radius: 18px;
            box-shadow: 0 4px 32px rgba(207,181,59,0.10);
            padding: 32px 28px 32px 28px;
        }
        h1 {
            color: #CFB53B;
            font-size: 2.1em;
            margin-bottom: 0.2em;
        }
        .subtitle {
            color: #333;
            font-size: 1.15em;
            margin-bottom: 1.2em;
        }
        #table-container {
            margin-top: 18px;
        }
        .button {
            margin: 18px 8px 0 0;
            padding: 10px 24px;
            background: linear-gradient(90deg, #CFB53B 0%, #FFD700 100%);
            color: #222;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 1.08em;
            font-weight: 600;
            box-shadow: 0 2px 8px rgba(207,181,59,0.08);
            transition: background 0.2s;
        }
        .button:hover {
            background: linear-gradient(90deg, #FFD700 0%, #CFB53B 100%);
        }
        .hot {
            border-radius: 10px !important;
            overflow: hidden;
            box-shadow: 0 2px 8px rgba(207,181,59,0.08);
        }
        .totals-row {
            background: #FFFBEA !important;
            font-weight: bold !important;
            color: #CFB53B !important;
        }
        .scenario-buttons {
            margin-bottom: 10px;
        }
        .lean-info-box, .standard-info-box, .growth-info-box {
            display: none;
            margin-bottom: 18px;
            padding: 14px 18px;
            background: #FFFBEA;
            border-left: 6px solid #CFB53B;
            border-radius: 8px;
            color: #333;
            font-size: 1.08em;
            font-weight: 500;
            box-shadow: 0 2px 8px rgba(207,181,59,0.08);
        }
        .lean-info-box.visible,
        .standard-info-box.visible,
        .growth-info-box.visible {
            display: block;
            animation: fadeIn 0.4s;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-10px);}
            to { opacity: 1; transform: translateY(0);}
        }
    </style>
</head>
<body>
    <div class='main-wrap'>
        <h1>Interaktive Forecast Tabelle</h1>
        <div class='subtitle'>Bearbeite die <b>Stückzahl</b> direkt in der Tabelle. Alle Berechnungen werden automatisch aktualisiert. Die Tabelle kann als Excel-Datei exportiert werden.</div>
        <div class='subtitle'>Die folgenden 3 Szenarien sind vorstellbar und stehen per Voreinstellung zur Verfügung:</div>
        <div class='scenario-buttons'>
            <button id='lean-btn' class='button'>Lean</button>
            <button id='standard-btn' class='button'>Standard</button>
            <button id='growth-btn' class='button'>Growth</button>
        </div>
        <div id='lean-info' class='lean-info-box'>
            <u>Lean-Szenario</u>
            <br><b>Gesamt-Investitionssumme:</b> € 88.250 (EK) + € 17.220 (Fixkosten) = <b>€ 105.950</b></br>
            <br><i>(Die weiteren Kosten fallen erst im operativen Geschäft an)</i></br>
            <br><b>Gesamt-Stückzahl:</b> 6.700<br>
        </div>
        <div id='standard-info' class='standard-info-box'>
            <u>Standard-Szenario</u>
            <br><b>Gesamt-Investitionssumme:</b> € 159.920 (EK) + € 30.150 (Fixkosten) = <b>€ 190.070</b></br>
            <br><i>(Die weiteren Kosten fallen erst im operativen Geschäft an)</i></br>
            <br><b>Gesamt-Stückzahl:</b> 11.250</br>
        </div>
        <div id='growth-info' class='growth-info-box'>
            <u>Growth-Szenario</u>
            <br><b>Gesamt-Investitionssumme:</b> € 337.725 (EK) + € 65.500 (Fixkosten) = <b>€ 403.225</b></br>
            <br><i>(Die weiteren Kosten fallen erst im operativen Geschäft an)</i></br>
            <br><b>Gesamt-Stückzahl:</b> 24.475</br>
        </div>
        <div id='table-container'></div>
        <button id='download-button' class='button'>Tabelle als Excel herunterladen</button>
    </div>
    <script>
        // Szenario Stückzahlen
        const scenarioStueckzahlen = {
            "Lean":    [1000,800,0,1000,0,0,0,0,500,0,1000,0,0,0,0,0,0,1650,0,750,0,0,0],
            "Standard":[1500,800,0,1500,800,0,750,0,500,0,1000,800,0,0,0,0,0,2300,500,800,0,0,0],
            "Growth":  [2000,1500,1000,2000,1000,1000,500,500,500,500,1000,1000,800,350,800,500,1000,3925,2000,2000,250,250,100]
        };

        // Initial data (23 Produkte, COGS/VK-Preis from user)
        const initialData = [
            ["Weste 1", 16, 120, 2000],
            ["Weste 2", 19, 130, 1500],
            ["Weste 3", 21, 150, 1000],
            ["Hausschuhe 1", 21, 79, 2000],
            ["Hausschuhe 2", 22, 79, 1000],
            ["Hausschuhe 3", 15, 89, 1000],
            ["Handschuhe 1", 24, 97, 1500],
            ["Handschuhe 2", 27, 117, 1000],
            ["Jacken 1", 19, 130, 800],
            ["Jacken 2", 20, 130, 600],
            ["Hoodie-Decken 1", 18, 70, 1200],
            ["Hoodie-Decken 2", 16, 60, 800],
            ["Heizdecke", 29, 129, 700],
            ["Kinderwagen-Griffe", 10, 59, 900],
            ["Socken", 10, 49, 1200],
            ["Sohlen", 5, 39, 1000],
            // Set VK-Preis for "Handwärmer-Banks" to 39
            ["Handwärmer-Banks", 9, 39, 2000],
            ["Powerbanks", 5, 19, 3925],
            ["Akkus", 3, 13, 2000],
            ["Ersatz-Kabel", 0.4, 4, 2000],
            ["Infrarot-Masken", 40, 219, 1000],
            ["Infrarot Caps", 32, 179, 900],
            ["IR-Matratzenauflagen", 76, 229, 800]
        ];

        // Function to round to two decimal places
        function round2(val) {
            return Math.round((val + Number.EPSILON) * 100) / 100;
        }

        // Function to calculate derived columns
        function recalculateTable(data) {
            // Indices for special products
            const specialProducts = {
                "Powerbanks": 17,
                "Akkus": 18,
                "Ersatz-Kabel": 19
            };

            return data.map((row, idx) => {
                if (!row[1] || !row[2] || typeof row[3] === "undefined") return row;
                const cogs = parseFloat(row[1]);
                const vkPreis = parseFloat(row[2]);
                const stueckzahl = parseFloat(row[3]);

                // If Stückzahl is 0, set all calculated columns to 0
                if (stueckzahl === 0) {
                    return [
                        row[0], round2(cogs), round2(vkPreis), 0, // Produkt, COGS, VK-Preis, Stückzahl
                        0, // Umsatz
                        round2(vkPreis - cogs), // DB je Einheit (still show)
                        0, // Gesamt-DB
                        vkPreis ? round2(((vkPreis - cogs) / vkPreis) * 100) : 0, // DB-Marge
                        0, // Gesamt-EK
                        0, // Lager
                        0, // Marketing
                        0, // Shipping
                        0, // Retouren
                        0, // Fixkosten
                        0, // Gesamtkosten
                        0, // EBITDA
                        0  // ROI
                    ];
                }

                const umsatz = round2(vkPreis * stueckzahl);
                const dbJeEinheit = round2(vkPreis - cogs);
                const gesamtDb = round2(dbJeEinheit * stueckzahl);
                const dbMarge = vkPreis ? round2((dbJeEinheit / vkPreis) * 100) : 0;
                const einkaufskosten = round2(cogs * stueckzahl);

                // Default calculations
                let lagergebuehren = round2(stueckzahl * 2); // Beispielwert
                let marketingkosten = round2(umsatz * 0.18);
                let shipping = round2(stueckzahl * 15);
                let retourenGebuehren = round2(stueckzahl * 1.5);

                // Special rules for Powerbanks, Akkus, Ersatz-Kabel
                let fixkosten;
                if (idx === specialProducts["Powerbanks"] || idx === specialProducts["Akkus"] || idx === specialProducts["Ersatz-Kabel"]) {
                    marketingkosten = 0;
                    shipping = 0;
                    retourenGebuehren = round2(stueckzahl * 0.75);
                    fixkosten = round2(stueckzahl * 3 * 0.6); // Reduce Fixkosten by 40%
                } else {
                    fixkosten = round2(stueckzahl * 3);
                }

                const gesamtkosten = round2(einkaufskosten + lagergebuehren + marketingkosten + shipping + retourenGebuehren + fixkosten);
                const ebitda = round2(umsatz - gesamtkosten);
                const roi = gesamtkosten > 0 ? round2(ebitda / gesamtkosten) : 0;

                return [
                    row[0], round2(cogs), round2(vkPreis), round2(stueckzahl), umsatz, dbJeEinheit, gesamtDb, dbMarge,
                    einkaufskosten, lagergebuehren, marketingkosten, shipping, retourenGebuehren,
                    fixkosten, gesamtkosten, ebitda, roi
                ];
            });
        }

        // Function to calculate totals row
        function calculateTotals(data) {
            // Only sum numeric columns, leave COGS, VK-Preis, DB, DB-Marge, Stückzahl blank
            let totals = [
                "Summe", "", "", "", 0, "", 0, "", 0, 0, 0, 0, 0, 0, 0, 0, 0
            ];
            for (let i = 0; i < data.length; i++) {
                let row = data[i];
                // Skip the totals row if present (to avoid double counting)
                if (row[0] === "Summe") continue;
                // Umsatz (4), Gesamt-DB (6), Gesamt-EK (8), Lager (9), Marketing (10), Shipping (11), Retouren (12), Fixkosten (13), Gesamtkosten (14), EBITDA (15), ROI (16)
                totals[4] += typeof row[4] === "number" && !isNaN(row[4]) ? row[4] : Number(row[4]) || 0;
                totals[6] += typeof row[6] === "number" && !isNaN(row[6]) ? row[6] : Number(row[6]) || 0;
                totals[8] += typeof row[8] === "number" && !isNaN(row[8]) ? row[8] : Number(row[8]) || 0;
                totals[9] += typeof row[9] === "number" && !isNaN(row[9]) ? row[9] : Number(row[9]) || 0;
                totals[10] += typeof row[10] === "number" && !isNaN(row[10]) ? row[10] : Number(row[10]) || 0;
                totals[11] += typeof row[11] === "number" && !isNaN(row[11]) ? row[11] : Number(row[11]) || 0;
                totals[12] += typeof row[12] === "number" && !isNaN(row[12]) ? row[12] : Number(row[12]) || 0;
                totals[13] += typeof row[13] === "number" && !isNaN(row[13]) ? row[13] : Number(row[13]) || 0;
                totals[14] += typeof row[14] === "number" && !isNaN(row[14]) ? row[14] : Number(row[14]) || 0;
                totals[15] += typeof row[15] === "number" && !isNaN(row[15]) ? row[15] : Number(row[15]) || 0;
                totals[16] += typeof row[16] === "number" && !isNaN(row[16]) ? row[16] : Number(row[16]) || 0;
            }
            // Round numeric totals
            [4,6,8,9,10,11,12,13,14,15,16].forEach(idx => {
                totals[idx] = round2(totals[idx]);
            });
            // For ROI (16), show overall ROI as EBITDA/Gesamtkosten if Gesamtkosten > 0
            totals[16] = totals[14] > 0 ? round2(totals[15] / totals[14]) : 0;
            // Stückzahl (3) left blank
            totals[3] = "";
            return totals;
        }

        // Function to render the table
        function renderTable(data) {
            const columns = [
                "Produkt", "COGS", "VK-Preis", "Stückzahl", "Umsatz",
                "DB", "Gesamt-DB", "DB-Marge", "Gesamt-EK",
                "Lager", "Marketing", "Shipping",
                "Retouren", "Fixkosten", "Gesamtkosten",
                "EBITDA", "ROI"
            ];

            // Calculate totals row
            const totalsRow = calculateTotals(data);

            // Data for Handsontable: add totals row at the end
            const tableData = [...data, totalsRow];

            if (window.hot) {
                window.hot.destroy();
            }

            window.hot = new Handsontable(document.getElementById('table-container'), {
                data: tableData,
                colHeaders: columns,
                rowHeaders: true,
                licenseKey: "non-commercial-and-evaluation",
                stretchH: "all",
                columns: [
                    { data: 0, type: "text", readOnly: true }, // Produkt
                    { data: 1, type: "numeric", readOnly: true }, // COGS
                    { data: 2, type: "numeric", readOnly: true }, // VK-Preis
                    { data: 3, type: "numeric", className: 'htLeft highlight-stueckzahl' }, // Stückzahl (editable)
                    { data: 4, type: "numeric", readOnly: true }, // Umsatz
                    { data: 5, type: "numeric", readOnly: true }, // DB
                    { data: 6, type: "numeric", readOnly: true }, // Gesamt-DB
                    { data: 7, type: "numeric", readOnly: true }, // DB-Marge
                    { data: 8, type: "numeric", readOnly: true }, // Gesamt-EK
                    { data: 9, type: "numeric", readOnly: true }, // Lagergebühren
                    { data: 10, type: "numeric", readOnly: true }, // Marketingkosten
                    { data: 11, type: "numeric", readOnly: true }, // Shipping
                    { data: 12, type: "numeric", readOnly: true }, // Retouren-Gebühren
                    { data: 13, type: "numeric", readOnly: true }, // Fixkosten
                    { data: 14, type: "numeric", readOnly: true }, // Gesamtkosten
                    { data: 15, type: "numeric", readOnly: true }, // EBITDA
                    { data: 16, type: "numeric", readOnly: true } // ROI
                ],
                afterChange: (changes, source) => {
                    if (source === "edit") {
                        const updatedData = recalculateTable(window.hot.getSourceData().slice(0, -1));
                        renderTable(updatedData); // re-render to update totals row
                    }
                },
                cells: function(row, col) {
                    var cellProperties = {};
                    // Totals row styling
                    if (row === this.instance.countRows() - 1) {
                        cellProperties.readOnly = true;
                        cellProperties.className = (cellProperties.className || '') + ' totals-row';
                    }
                    // Stückzahl editable except totals row
                    if (col === 3 && row !== this.instance.countRows() - 1) {
                        cellProperties.renderer = function(instance, td, row, col, prop, value, cellProperties) {
                            Handsontable.renderers.NumericRenderer.apply(this, arguments);
                            td.style.background = '#FFFBEA';
                            td.style.fontWeight = 'bold';
                            td.style.border = '2px solid #FFD700';
                        };
                    }
                    return cellProperties;
                }
            });
        }

        // Initial render
        let recalculatedData = recalculateTable(initialData);
        renderTable(recalculatedData);

        // Download handler
        document.getElementById('download-button').addEventListener('click', () => {
            // Exclude the totals row from export if you want, or include it
            const data = window.hot.getData();
            const ws = XLSX.utils.aoa_to_sheet(data);
            const wb = XLSX.utils.book_new();
            XLSX.utils.book_append_sheet(wb, ws, "Sheet1");
            XLSX.writeFile(wb, "investment_case_table.xlsx");
        });

        // Szenario Button Handlers
        function setScenario(scenario) {
            // Get current table data (except totals row)
            let data = window.hot.getSourceData().slice(0, -1);
            let stueckzahlen = scenarioStueckzahlen[scenario];
            // Set Stückzahl for each row
            for (let i = 0; i < data.length; i++) {
                data[i][3] = stueckzahlen[i] !== undefined ? stueckzahlen[i] : 0;
            }
            let recalculated = recalculateTable(data);
            renderTable(recalculated);

            // Show/hide info boxes for all scenarios
            var leanBox = document.getElementById('lean-info');
            var standardBox = document.getElementById('standard-info');
            var growthBox = document.getElementById('growth-info');
            leanBox.classList.remove('visible');
            standardBox.classList.remove('visible');
            growthBox.classList.remove('visible');
            if (scenario === 'Lean') {
                leanBox.classList.add('visible');
            } else if (scenario === 'Standard') {
                standardBox.classList.add('visible');
            } else if (scenario === 'Growth') {
                growthBox.classList.add('visible');
            }
        }

        document.getElementById('lean-btn').addEventListener('click', function() {
            setScenario('Lean');
        });
        document.getElementById('standard-btn').addEventListener('click', function() {
            setScenario('Standard');
        });
        document.getElementById('growth-btn').addEventListener('click', function() {
            setScenario('Growth');
        });
    </script>
</body>
</html>
"""

# Embed the custom HTML and JavaScript in Streamlit
st.title("Szenario Casting")
components.html(custom_html, height=900, scrolling=True)
