import streamlit as st
st.set_page_config(page_title="Konkurrenzanalyse USA", layout="wide")
def show():
    st.header("Der Markt heute: Dominiert von austauschbaren China-Marken")

    # Custom CSS for table
    st.markdown(
        """
        <style>
        .konkurrenz-table th, .konkurrenz-table td { padding: 7px 10px; text-align: center; font-size: 1em; }
        .konkurrenz-table th { background: #f5f5f5; font-weight: 600; }
        .konkurrenz-table { border-collapse: collapse; margin-bottom: 18px; }
        .konkurrenz-table td, .konkurrenz-table th { border: 1px solid #e0e0e0; }
        .highlight-china { background: #ffe4b2 !important; color: #b25c00 !important; }
        .highlight-namenhaft { background: #cce5ff !important; color: #004085 !important; }
        .highlight-approach { background: #d4edda !important; color: #155724 !important; font-weight: 600; }
        </style>
        """,
        unsafe_allow_html=True
    )

    # State for highlighting
    china_highlight = st.session_state.get("china_highlight", False)
    namenhaft_highlight = st.session_state.get("namenhaft_highlight", False)
    china_price_highlight = st.session_state.get("china_price_highlight", False)
    marken_price_highlight = st.session_state.get("marken_price_highlight", False)
    kernaussage_highlight = st.session_state.get("kernaussage_highlight", False)
    approach_highlight = st.session_state.get("approach_highlight", False)

    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        if st.button("China-Marken"):
            st.session_state["china_highlight"] = True
            st.session_state["namenhaft_highlight"] = False
            st.session_state["china_price_highlight"] = False
            st.session_state["marken_price_highlight"] = False
            st.session_state["kernaussage_highlight"] = False
            st.session_state["approach_highlight"] = False
    with col2:
        if st.button("Namenhafte-Marken"):
            st.session_state["china_highlight"] = False
            st.session_state["namenhaft_highlight"] = True
            st.session_state["china_price_highlight"] = False
            st.session_state["marken_price_highlight"] = False
            st.session_state["kernaussage_highlight"] = False
            st.session_state["approach_highlight"] = False
    with col3:
        if st.button("China-Preisstrategie"):
            st.session_state["china_highlight"] = False
            st.session_state["namenhaft_highlight"] = False
            st.session_state["china_price_highlight"] = True
            st.session_state["marken_price_highlight"] = False
            st.session_state["kernaussage_highlight"] = False
            st.session_state["approach_highlight"] = False
    with col4:
        if st.button("Marken-Preisstrategie"):
            st.session_state["china_highlight"] = False
            st.session_state["namenhaft_highlight"] = False
            st.session_state["china_price_highlight"] = False
            st.session_state["marken_price_highlight"] = True
            st.session_state["kernaussage_highlight"] = False
            st.session_state["approach_highlight"] = False
    with col5:
        if st.button("Kernaussage"):
            st.session_state["china_highlight"] = False
            st.session_state["namenhaft_highlight"] = False
            st.session_state["china_price_highlight"] = False
            st.session_state["marken_price_highlight"] = False
            st.session_state["kernaussage_highlight"] = True
            st.session_state["approach_highlight"] = False
    with col6:
        if st.button("Unser Approach"):
            st.session_state["china_highlight"] = False
            st.session_state["namenhaft_highlight"] = False
            st.session_state["china_price_highlight"] = False
            st.session_state["marken_price_highlight"] = False
            st.session_state["kernaussage_highlight"] = False
            st.session_state["approach_highlight"] = True

    # Refresh local state after button clicks
    china_highlight = st.session_state.get("china_highlight", False)
    namenhaft_highlight = st.session_state.get("namenhaft_highlight", False)
    china_price_highlight = st.session_state.get("china_price_highlight", False)
    marken_price_highlight = st.session_state.get("marken_price_highlight", False)
    kernaussage_highlight = st.session_state.get("kernaussage_highlight", False)
    approach_highlight = st.session_state.get("approach_highlight", False)

    # Show all selected info boxes above the table
    if china_highlight:
        st.info("Diese China-Marken haben einen geschätzten Marktanteil von >51\\% und dabei mittelmäßige Bewertungen, die vermutlich zum großen Teil gekauft sind. Diese Marken dominieren den E-Commerce Markt und bieten austauschbare Produkte an, die sich kaum durch Qualität oder Branding unterscheiden.")
    if namenhaft_highlight:
        st.info("Diese Marken haben ein starkes Branding und sehr gutes Image, dafür jedoch verhältnismäßig wenig Marktanteil (Geschätzt 25 - 32\\%). Besonders die E-Commerce Präsenz ist schwach. Diese Marken sind in anderen Bereichen stark, jedoch nicht im Heizprodukte-Segment.")
    if china_price_highlight:
        st.info("China-Marken arbeiten mit stark überhöhten UVP, um über dauerhafte Rabatte (von bis zu 45\\%) Kaufanreize zu schaffen. Der Preis ist zentraler Teil des Kaufarguments – „Schnäppchen“-Effekt.")
    if marken_price_highlight:
        st.info("Etablierte Marken kalkulieren realitätsnäher, mit geringeren (ca. 15 - 20\\%) oder keinen Rabatten. Der Preis entspricht dem tatsächlichen Markenwert.")
    if kernaussage_highlight:
        st.info("China-Marken verkaufen über den Preis, etablierte Marken über Vertrauen. Wir kämpfen nicht gegen Patagonia & North Face, sondern gegen austauschbare AliExpress-Importe.")
    if approach_highlight:
        st.success(
            "Differenzierung über Qualität, Branding und Kundenerlebnis fehlt für Heizprodukte – genau das ist unsere Lücke am Markt! \n"
            "Wir kombinieren die Stärken der Competitor so, dass wir ein starkes Branding und hohe E-Commerce Kompetenz verknüpfen - Ohne Ramsch-Preise und mit sehr guten Kundenbewertungen."
        )

    # Table HTML with conditional highlights and clickable brand links
    brand_links = {
        "Ororo": "https://www.ororowear.com/",
        "Venustras": "https://venustasofficial.com/",
        "Gobi Heat": "https://gobiheat.com/",
        "TideWe": "https://www.tidewe.com/",
        "Gerbing": "https://gerbing.com/",
        "Milwaukee Tool": "https://www.milwaukeetool.com/Products/Heated-Gear",
        "Bosch": "https://www.boschtools.com/us/en/",
        "Makita": "https://www.makitatools.com/",
    }

    table_html = """
    <table class="konkurrenz-table">
        <tr>
            <th>Marke</th>
            <th>Herkunft</th>
            <th>Plattformen</th>
            <th>⌀-Bewertung</th>
            <th>Kerngeschäft</th>
            <th>Branding</th>
            <th>UVP</th>
            <th>tatsächlicher ⌀-Preis</th>
        </tr>
    """

    rows = [
        ["Ororo", "China", "Amazon, eigene Website", "~4,4 /5  (Amazon)", "Heizprodukte", "Alltags- & Outdoor-Bekleidung für urbane Nutzer", "~ $200", "~ $130 (Häufig reduziert)"],
        ["Venustras", "China", "Amazon, Walmart, eigene Website", "~4,3 /5  (Amazon)", "Heizprodukte", "Günstige Heizkleidung für den Alltag", "~ $180", "~ $150 (Sale)"],
        ["Gobi Heat", "China", "Amazon, eigene Website", "~4,1 /5  (Amazon)", "Heizprodukte", "Minimalistisch, praktisch, preisorientiert", "~ $150–$180", "~ $100–$120(Sale)"],
        ["TideWe", "China", "Amazon, eigene Website", "~4,2 /5  (Amazon)", "Heizprodukte", "Jagd- & Outdoor-Marke für Einsteiger", "~ $120–$150", "~ $100–$120(Sale)"],
        ["Gerbing", "USA", "Eigener Handel, Fachhandel", "~4,6 /5  (Amazon)","Heizprodukte", "Premium-Marke für Motorrad- & Extremsport", "~ $270–$400 (Heizjacke-Motorrad)", "~ $270–$400 (Festpreise)"],
        ["Milwaukee Tool", "USA", "Baumärkte, Amazon, Fachhandel", "~4,7 /5  (Amazon)", "Profi-Elektrowerkzeug", "Pro-Marke für Bau & Handwerk", "~ $200–$300 (Heizwesten)", "~ $180–$250 (Sale)"],
        ["Bosch", "Deutschland", "Baumärkte, Amazon, eigene Website", "~4,6 /5  (Amazon)", "Werkzeug & Innovation", "Technik- & Innovationsanspruch", "~ € 150–€ 250 (Heizwesten)", "~ € 130–€ 220 (Sale)"],
        ["Makita", "Japan", "Baumärkte, Amazon, eigene Website", "~4,7 /5  (Amazon)", "Werkzeug & Garten", "Präzision für Handwerk & Industrie", "~ $220–$320 (Heizwesten/-Matten)", "~ $200–$280 (Sale)"],
    ]

    namenhafte_marken = {"Milwaukee Tool", "Gerbing", "Bosch", "Makita"}

    for idx, row in enumerate(rows):
        marke, herkunft = row[0], row[1]
        marke_class = ""
        herkunft_class = ""
        bewertung_class = ""
        branding_class = ""
        uvp_class = ""
        preis_class = ""
        if china_highlight and herkunft == "China":
            herkunft_class = "highlight-china"
            bewertung_class = "highlight-china"
        if namenhaft_highlight and marke in namenhafte_marken:
            marke_class = "highlight-namenhaft"
            branding_class = "highlight-namenhaft"
        # Highlight UVP and Preis for first 4 rows if China-Preisstrategie is active
        if china_price_highlight and idx < 4:
            uvp_class = "highlight-china"
            preis_class = "highlight-china"
        # Highlight UVP and Preis for last 4 rows if Marken-Preisstrategie is active
        if marken_price_highlight and idx >= 4:
            uvp_class = "highlight-namenhaft"
            preis_class = "highlight-namenhaft"
        table_html += "<tr>"
        # Make brand clickable
        if marke in brand_links:
            table_html += f'<td class="{marke_class}"><a href="{brand_links[marke]}" target="_blank" style="color:inherit;text-decoration:underline;">{marke}</a></td>'
        else:
            table_html += f'<td class="{marke_class}">{marke}</td>'
        table_html += f'<td class="{herkunft_class}">{herkunft}</td>'
        # Plattformen
        table_html += f"<td>{row[2]}</td>"
        # ⌀-Bewertung
        table_html += f'<td class="{bewertung_class}">{row[3]}</td>'
        # Kerngeschäft
        table_html += f"<td>{row[4]}</td>"
        # Branding
        table_html += f'<td class="{branding_class}">{row[5]}</td>'
        # UVP
        table_html += f'<td class="{uvp_class}">{row[6]}</td>'
        # tatsächlicher Preis
        table_html += f'<td class="{preis_class}">{row[7]}</td>'
        table_html += "</tr>"

    # Add "Unsere Marke" row if approach_highlight is active
    if approach_highlight:
        approach_row = [
            "Unsere Marke",
            "DE/USA",
            "Amazon, eigene Website, Multichannel",
            "4,7/5 (Amazon)",
            "Heated Apparel",
            "Stylisch, Cozy & funktional top!",
            "$200",
            "$159 (Sale)"
        ]
        table_html += '<tr>'
        for val in approach_row:
            table_html += f'<td class="highlight-approach">{val}</td>'
        table_html += '</tr>'

    table_html += "</table>"

    st.markdown(table_html, unsafe_allow_html=True)

    # Pie chart with hover and clickable links
    import plotly.graph_objects as go
    brands = ["ORORO", "Venustas", "Gobi Heat", "TideWe", "Gerbing", "Milwaukee Tool", "Bosch", "Makita", "Andere"]
    shares = [19, 14, 10, 8, 8, 8, 8, 8, 17]
    # Pie chart links (used for clickable slices)
    links = [
        "https://www.ororowear.com/",
        "https://venustasofficial.com/",
        "https://gobiheat.com/",
        "https://www.tidewe.com/",
        "https://gerbing.com/",
        "https://www.milwaukeetool.com/Products/Heated-Gear",
        "https://www.boschtools.com/us/en/",
        "https://www.makitatools.com/",
        "https://www.amazon.com/s?k=heated+vest"
    ]

    # Show chart
    fig = go.Figure(data=[go.Pie(
        labels=brands,
        values=shares,
        hoverinfo="label+percent",
        textinfo="label",
        pull=[0.05]*len(brands),
        marker=dict(colors=["#FFD700", "#CFB53B", "#B0A160", "#7EC8E3", "#FFB6C1", "#1a237e", "#4CAF50", "#E57373", "#BDBDBD"]),
        customdata=links,
    )])
    fig.update_traces(
        hovertemplate="%{label}: %{percent}",
        textfont_size=14,
    )
    fig.update_layout(
        title_text="Marktanteile der Haupt-Konkurrenten",
        showlegend=False,
    )

    st.plotly_chart(fig, use_container_width=True)

    # Note: Plotly chart slices cannot be made clickable in Streamlit natively.
    # The script block below will not work in Streamlit, so it is removed.

show()