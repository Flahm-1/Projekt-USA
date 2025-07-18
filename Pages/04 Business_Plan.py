import streamlit as st

st.set_page_config(page_title="Roadmap", layout="wide")
st.header("Roadmap")

# --- Roadmap Timeline ---
st.markdown(
    """
    <style>
    .timeline {
        display: flex;
        align-items: flex-start;
        gap: 32px;
        margin: 32px 0 40px 0;
        overflow-x: auto;
    }
    .phase {
        background: #fffbe6;
        border: 2px solid #CFB53B;
        border-radius: 12px;
        min-width: 220px;
        max-width: 260px;
        padding: 18px 16px 14px 16px;
        box-shadow: 0 2px 8px rgba(207,181,59,0.08);
        position: relative;
        transition: box-shadow 0.2s, border-color 0.2s;
        cursor: pointer;
    }
    .phase:hover {
        box-shadow: 0 4px 16px rgba(207,181,59,0.18);
        border-color: #FFD700;
    }
    .phase-title {
        font-size: 1.08em;
        font-weight: 600;
        margin-bottom: 0.5em;
    }
    .phase-desc {
        font-size: 0.98em;
        color: #444;
        margin-bottom: 0.5em;
    }
    .phase-tooltip {
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
    .phase:hover .phase-tooltip {
        display: block;
    }
    </style>
    <div class="timeline">
        <div class="phase">
            <div class="phase-title">Q4/2025 – Vorbereitung & Sourcing</div>
            <div class="phase-desc">Lieferantenauswahl, Produkt-Sampling, Zertifizierungen, Quality Control</div>
            <div class="phase-tooltip">KPIs/To-dos:<br>- 3 geprüfte Lieferanten<br>- 2 Produktmuster<br>- CE/UL Zertifizierung<br>- QC-Report</div>
        </div>
        <div class="phase">
            <div class="phase-title">Q1-Q2/2026 – Launch Phase</div>
            <div class="phase-desc">Amazon.com & Shopify Go-Live, Social Proof, Ads</div>
            <div class="phase-tooltip">KPIs/To-dos:<br>- 50+ Bewertungen<br>- 3 Influencer-Kooperationen<br>- 1.000+ Follower<br>- 1. Kampagne live</div>
        </div>
        <div class="phase">
            <div class="phase-title">Q3/2026 – Marketing-Skalierung</div>
            <div class="phase-desc">Retargeting, Lookalikes, Affiliate-Netzwerk</div>
            <div class="phase-tooltip">KPIs/To-dos:<br>- 5 Affiliate-Partner<br>- 2 Retargeting-Kampagnen<br>- 10% ROAS-Steigerung</div>
        </div>
        <div class="phase">
            <div class="phase-title">Q4/2026 – Automatisierung & Skalierung</div>
            <div class="phase-desc">Fulfillment, Support, DTC Brand Building</div>
            <div class="phase-tooltip">KPIs/To-dos:<br>- 24h Versand<br>- 95% Kundenzufriedenheit<br>- 2 neue Wiederverkäufer</div>
        </div>
        <div class="phase">
            <div class="phase-title">Q1/2027 – Sortimentserweiterung</div>
            <div class="phase-desc">Einführung: Heizjacken, Socken, IR-Produkte<br>B2B-Kanäle testen (z. B. REI, Walmart Marketplace)</div>
            <div class="phase-tooltip">KPIs/To-dos:<br>- 3 neue Produktlinien<br>- 2 B2B-Kanäle getestet<br>- 1 B2B-Partner gewonnen</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Business Model Canvas ---
st.subheader("Business Modell Canvas")
st.markdown(
    """
    <div style="display: flex; justify-content: center; margin-top: 24px;">
        <img src="https://cdn.shopify.com/s/files/1/0646/7757/6971/t/1/assets/Business%20Modell%20Canvas%20Projekt%20USA.jpg?v=1752669659" alt="Business Modell Canvas" style="max-width: 90%; border-radius: 12px; box-shadow: 0 2px 12px rgba(0,0,0,0.12);">
    </div>
    """,
    unsafe_allow_html=True
)