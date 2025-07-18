
import streamlit as st

st.set_page_config(page_title="Exit-Strategien & Chancen für Investoren", layout="wide")

# --- Exit-Optionen Vergleich ---
st.markdown("""
<div style='font-size:1.13em; font-weight:400; margin-bottom:0.2em; color:#1A2942;'>Optionen im Vergleich</div>
""", unsafe_allow_html=True)
st.markdown(
    """
    <style>
    .exit-table {
        width: 100%;
        max-width: 800px;
        margin: 0 auto 24px auto;
        border-collapse: separate;
        border-spacing: 0;
        font-size: 1.08em;
        box-shadow: 0 2px 12px rgba(26,41,66,0.07);
    }
    .exit-table th, .exit-table td {
        padding: 12px 18px;
        border-bottom: 1.5px solid #eee;
        text-align: center;
    }
    .exit-table th {
        background: #f7f7fa;
        font-weight: 600;
        color: #1A2942;
    }
    .exit-table td {
        background: #fff;
    }
    .exit-tooltip {
        display: inline-block;
        position: relative;
        cursor: pointer;
        color: #CFB53B;
        font-size: 1.1em;
        margin-left: 6px;
    }
    .exit-tooltip .exit-tooltiptext {
        visibility: hidden;
        width: 260px;
        background: #fffbe6;
        color: #222;
        text-align: left;
        border-radius: 8px;
        border: 1.5px solid #CFB53B;
        padding: 10px 14px;
        position: absolute;
        z-index: 10;
        bottom: 120%;
        left: 50%;
        transform: translateX(-50%);
        opacity: 0;
        transition: opacity 0.2s;
        font-size: 0.98em;
        box-shadow: 0 2px 8px rgba(207,181,59,0.10);
    }
    .exit-tooltip:hover .exit-tooltiptext {
        visibility: visible;
        opacity: 1;
    }
    </style>
    <table class="exit-table">
        <tr>
            <th>Strategie</th>
            <th>Beschreibung</th>
            <th>Vorteil für Investoren <span class="exit-tooltip">🟡<span class="exit-tooltiptext">Strategische Exit-Möglichkeiten: Empire Flippers, Exit.io oder Aaron Cordovez</span></span></th>
        </tr>
        <tr>
            <td><b>Build-to-Sell</b></td>
            <td>Skalieren bis zur Übernahme durch Private Investor, Aggregator oder Brand-Rollup-Plattform</td>
            <td>Liquiditätsereignis nach 2–3 Jahren möglich</td>
        </tr>
        <tr>
            <td><b>Build-to-Hold</b></td>
            <td>Marke dauerhaft betreiben, jährlich 6- bis 7-stellige Ausschüttungen</td>
            <td>Passives Einkommen, Markenwert steigt</td>
        </tr>
    </table>
    """,
    unsafe_allow_html=True
)

# --- Bewertungshebel Visual ---
st.markdown("""
<div style='font-size:1.13em; font-weight:400; margin-bottom:0.2em; color:#1A2942;'>Bewertungshebel: So steigern wir den Unternehmenswert</div>
""", unsafe_allow_html=True)
st.markdown(
    """
    <style>
    .hebel-row {
        display: flex;
        gap: 32px;
        justify-content: center;
        margin: 32px 0 24px 0;
    }
    .hebel-box {
        background: #fffbe6;
        border: 2px solid #CFB53B;
        border-radius: 14px;
        min-width: 180px;
        max-width: 220px;
        padding: 22px 14px 18px 14px;
        text-align: center;
        font-size: 1.08em;
        font-weight: 500;
        position: relative;
        box-shadow: 0 2px 8px rgba(207,181,59,0.10);
        transition: box-shadow 0.2s, border-color 0.2s;
        cursor: pointer;
        animation: hebelpop 1.2s cubic-bezier(.68,-0.55,.27,1.55) both;
    }
    .hebel-box:hover {
        box-shadow: 0 4px 16px rgba(207,181,59,0.18);
        border-color: #FFD700;
    }
    @keyframes hebelpop {
        0% { transform: scale(0.8); opacity: 0.2; }
        80% { transform: scale(1.08); opacity: 1; }
        100% { transform: scale(1); }
    }
    .hebel-icon {
        font-size: 2.1em;
        margin-bottom: 0.18em;
        display: block;
        transition: transform 0.2s;
    }
    .hebel-box:hover .hebel-icon {
        transform: scale(1.18) rotate(-8deg);
    }
    .hebel-tooltip {
        display: none;
        position: absolute;
        left: 50%;
        top: 100%;
        transform: translateX(-50%);
        background: #fff;
        border: 1.5px solid #CFB53B;
        border-radius: 8px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        padding: 10px 14px;
        font-size: 0.97em;
        color: #222;
        z-index: 10;
        min-width: 180px;
        margin-top: 8px;
    }
    .hebel-box:hover .hebel-tooltip {
        display: block;
    }
    </style>
    <div class="hebel-row">
        <div class="hebel-box">
            <span class="hebel-icon">™️</span>
            Branding & Design
            <div class="hebel-tooltip">Premium-Look, Wiedererkennung & Eigenentwicklung</div>
        </div>
        <div class="hebel-box">
            <span class="hebel-icon">📈</span>
            Umsatzwachstum
            <div class="hebel-tooltip">Gewinnthesaurierung in Multichannel + Portfolio</div>
        </div>
        <div class="hebel-box">
            <span class="hebel-icon">🔁</span>
            Kundenbindung
            <div class="hebel-tooltip">E-Mail, Up-selling, Brand Image, Wiederkäufe</div>
        </div>
        <div class="hebel-box">
            <span class="hebel-icon">⚙️</span>
            Prozesseffizienz
            <div class="hebel-tooltip">Remote Setups, Automatisierung durch Tools</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")

# --- Beispielhafte Unternehmensbewertungen ---
st.markdown("""
<div style='font-size:1.13em; font-weight:400; margin-bottom:0.2em; color:#1A2942;'>Beispielhafte Unternehmensbewertungen</div>
""", unsafe_allow_html=True)

bewertungen = [
    {
        "titel": "'Lean'-Umsatz Year 1",
        "umsatz": 472_000,
        "ebitda": 0.34,
        "multiple_min": 3,
        "multiple_max": 5
    },
    {
        "titel": "'Standard'-Umsatz Year 1",
        "umsatz": 775_000,
        "ebitda": 0.30,
        "multiple_min": 3,
        "multiple_max": 5
    },
    {
        "titel": "'Growth'-Umsatz Year 1",
        "umsatz": 1_700_000,
        "ebitda": 0.33,
        "multiple_min": 3,
        "multiple_max": 5
    }
]

# Drei Spalten nebeneinander
col1, col2, col3 = st.columns(3)
cols = [col1, col2, col3]

for i, b in enumerate(bewertungen):
    ebitda_betrag = b["umsatz"] * b["ebitda"]
    bewertung_min = ebitda_betrag * b["multiple_min"]
    bewertung_max = ebitda_betrag * b["multiple_max"]
    umsatz_str = f"{b['umsatz'] // 1000:,} TSD $".replace(",", ".")
    ebitda_str = f"{int(b['ebitda']*100)} %"
    bewertungsspanne = f"{int(bewertung_min):,} – {int(bewertung_max):,} $".replace(",", ".")
    box_html = f"""
        <div style='max-width:320px; margin:0 auto 0.5em auto; background:#f7f7fa; border-radius:10px; border:2px solid #CFB53B; padding:16px 10px;'>
            <div style='font-size:1.07em; font-weight:600; margin-bottom:0.4em;'>{b['titel']}: <span style='color:#1A2942;'>{umsatz_str}</span></div>
            <div style='font-size:1em; margin-bottom:0.4em;'>EBITDA Marge: <span style='color:#1A2942;'>{ebitda_str}</span></div>
            <div style='font-size:1em; margin-bottom:0.4em;'>Bewertungs-Multiple: <span style='color:#1A2942;'>{b['multiple_min']}x–{b['multiple_max']}x</span></div>
            <div style='font-size:1.08em; font-weight:700; color:#CFB53B; margin-bottom:0.4em;'>🟠 Bewertungsspanne: {bewertungsspanne}</div>
        </div>
    """
    cols[i].markdown(box_html, unsafe_allow_html=True)

st.markdown(
    "<div style='text-align:center; margin-top:0.5em; font-style:italic; color:#444; font-size:1.01em;'>Konservativ gerechnet – höherer Multiple bei Markenstärke und Repeat-Käufen möglich.</div>",
    unsafe_allow_html=True
)

