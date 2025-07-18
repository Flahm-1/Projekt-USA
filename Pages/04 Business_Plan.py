import streamlit as st

st.set_page_config(page_title="Roadmap", layout="wide")
st.header("Roadmap")
# --- Roadmap Timeline with Clickable Blocks ---

# Define roadmap phases and tooltips
phases = [
    {
        "title": "Q4/2025 – Vorbereitung & Sourcing",
        "desc": "Lieferantenauswahl, Produkt-Sampling, Zertifizierungen, Quality Control",
        "tooltip": "KPIs/To-dos:\n- 3 geprüfte Lieferanten (Vor Ort - Messe Canton & Factory-Besuch)\n- Diverse Produktmuster abegestimmt & 'golden'-Sample fertig\n- CE/FCC Zertifizierung\n- QC-Reports\n- Produktshooting und Listing Vorbereitung"
    },
    {
        "title": "Q1-Q2/2026 – Launch Phase",
        "desc": "Amazon.com & Shopify Go-Live, Social Proof, Ads",
        "tooltip": "KPIs/To-dos:\n- 50+ Bewertungen je Produkt (AMZ Vine)\n- UGC & Micro-/Mini-Influencer-Kooperationen\n- Aufbau Social Media Kanäle +1000 Follower (GetCloud)\n- 1. PPC Kampagne pro Kanal live"
    },
    {
        "title": "Q3/2026 – Marketing-Aufbau",
        "desc": "Affiliate-Netzwerk, PPC Kampagnen On-/Offsite, Social Media Ads",
        "tooltip": "KPIs/To-dos:\n- Zusammenarbeit mit Affiliate-Partnern\n- Vollständiges Kampagnen-Setup\n- Preis und CPC optimieren (Profasee)\n- Social Media Ads launchen"
    },
    {
        "title": "Q4/2026 – Automatisierung & Skalierung",
        "desc": "Prozesse automatisieren, Support delegieren und SLA implementieren, DTC Brand Building",
        "tooltip": "KPIs/To-dos:\n- Support KI anlernen\n- 95% Kundenzufriedenheit\n- Teams einarbeiten\n- Versand und Retouren optimieren & nachverhandeln"
    },
    {
        "title": "Q1/2027 – Sortimentserweiterung",
        "desc": "- Kollektion erweitern \n- Weitere Vertriebskanäle aufbauen (z. B. Walmart, Etsy, Ebay)",
        "tooltip": "KPIs/To-dos:\n- Neue Produktlinien (Modelle, Kühlprodukte und Ähnliches)\n-  Multichannel-Kanäle anbinden\n- Ggf. Großhandelspartner gewinnen"
    },
]

# Custom CSS for equal block sizes and style
st.markdown("""
<style>
.roadmap-container {
    display: flex;
    gap: 32px;
    margin: 32px 0 40px 0;
    overflow-x: auto;
}
.roadmap-block {
    background: #fffbe6;
    border: 2px solid #CFB53B;
    border-radius: 12px;
    min-width: 240px;
    max-width: 240px;
    min-height: 180px;
    max-height: 180px;
    padding: 18px 16px 14px 16px;
    box-shadow: 0 2px 8px rgba(207,181,59,0.08);
    position: relative;
    transition: box-shadow 0.2s, border-color 0.2s;
    cursor: pointer;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
}
.roadmap-block-selected {
    border-color: #FFD700 !important;
    box-shadow: 0 4px 16px rgba(207,181,59,0.18);
}
.roadmap-title {
    font-size: 1.08em;
    font-weight: 600;
    margin-bottom: 0.5em;
}
.roadmap-desc {
    font-size: 0.98em;
    color: #444;
    margin-bottom: 0.5em;
}
.phase-btn-label {
    font-weight: 600;
    font-size: 1.1em;
    color: #CFB53B;
    margin-bottom: 0.7em;
    letter-spacing: 0.04em;
}
</style>
""", unsafe_allow_html=True)

# Use session state to track which block is selected
if "selected_phase" not in st.session_state:
    st.session_state.selected_phase = None

# Render roadmap blocks as columns
cols = st.columns(len(phases), gap="large")
for idx, (col, phase) in enumerate(zip(cols, phases)):
    with col:
        # Use a button for each block
        btn_key = f"phase_btn_{idx}"
        block_class = "roadmap-block"
        if st.session_state.selected_phase == idx:
            block_class += " roadmap-block-selected"
        # Render block as HTML button for style, with phase label
        st.markdown(
            f"""
            <button class="{block_class}" style="width:100%;border:none;background:none;padding:0;" onclick="window.dispatchEvent(new CustomEvent('selectPhase{idx}'));">
                <div class="phase-btn-label">Phase {idx+1}</div>
                <div class="roadmap-title">{phase['title']}</div>
                <div class="roadmap-desc">{phase['desc']}</div>
            </button>
            """,
            unsafe_allow_html=True
        )
        # Add a hidden Streamlit button to trigger selection
        if st.button(f"Phase {idx+1}", key=btn_key, help=phase['title']):
            st.session_state.selected_phase = idx

# Show the tooltip textbox below the timeline if a block is selected
if st.session_state.selected_phase is not None:
    selected = phases[st.session_state.selected_phase]
    st.info(f"**{selected['title']}**\n\n{selected['tooltip']}")

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