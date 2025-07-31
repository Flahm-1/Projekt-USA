import streamlit as st
import streamlit_echarts as st_echarts
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Heated Apparel Dashboard",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="🔥"
)

# Inject custom CSS for frame box and hover effect
st.markdown(
    """
    <style>
    .frame-box {
        border:2px solid #1A2942;
        border-radius:10px;
        padding:12px;
        margin-bottom:10px;
        display:flex;
        flex-direction:column;
        justify-content:center;
        transition: box-shadow 0.2s, border-color 0.2s;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    }
    .frame-box:hover {
        box-shadow: 0 4px 16px rgba(207,181,59,0.18);
        border-color: #CFB53B;
        background: #FFFBEA;
    }
    </style>
    """,
    unsafe_allow_html=True
)

CONTAINER_STYLE = ""

def show():
    st.markdown(
        """
        <div style='text-align:center; margin-bottom:1em;'>
            <span style='color:black; font-size:2em; font-weight:bold;'>Heated Apparel:</span><br>
            <span style='color:black; font-size:2em; font-weight:bold;'>Mit Premium-Heatwear den US-Markt erobern</span><br>
            <span style='font-size:2em; font-weight:bold;'>& <span style='color:red;'>10X</span> wachsen</span>
        </div>
        """,
        unsafe_allow_html=True
    )
   

    st.write("")
    colA, colB = st.columns(2)
    FRAME_MIN_HEIGHT = "220px"  # Adjust as needed for your content

    with colA:
        with st.container():
            # Removed frame-box for this section
            st.markdown(
                """
                <div style='font-size:19px;'>
                <strong>Aktuelle Situation in Deutschland</strong>
                
                  <span style='color:red;'>-</span> Schwindende Nettogewinne trotz steigender Handelsmargen  
                  <span style='color:red;'>-</span> Sinkende Nachfrage durch Überangebot und Inflation  
                  <span style='color:red;'>-</span> Schwache Marktentwicklung mit niedrigem Wachstumspotential  
                  <span style='color:red;'>-</span> Steigende Bürokratie-Kosten und Unsicherheit durch anhaltende Rezession 

                </div>
                """,
                unsafe_allow_html=True
            )
        with st.container():
            st.markdown(
                f"""
                <div class='frame-box' style='min-height:{FRAME_MIN_HEIGHT};'>

                **Zahlungsbereitschaft**

                Im US-Apparel-Segment geben Kunden durchschnittlich $162/Monat für Kleidung & Services aus. 40% des US-Apparel-E-Commerce-Markts entfallen auf Premium-Marken, was auf starke Kaufkraft im Premiumbereich hinweist  
                [Quelle](https://www.oberlo.com/statistics/how-much-do-people-spend-on-clothes)
                </div>
                """,
                unsafe_allow_html=True
            )
        with st.container():
            st.markdown(
                f"""
                <div class='frame-box' style='min-height:{FRAME_MIN_HEIGHT};'>

                **USA größter E-Com Markt**

                1192 Mrd. USD Online-Retail-Volumen in den USA - Davon rund 145 Mrd. USD für Bekleidung (Stand 2024)  
                [Quelle](https://www.marketplacepulse.com/stats/us-e-commerce-sales-unadjusted)
                </div>
                """,
                unsafe_allow_html=True
            )

    with colB:
        with st.container():
            # Removed frame-box for this section
            st.markdown(
                """
                <div style='font-size:19px;'>
                <strong>USA-Markt Potentiale</strong>
                
                  <span style='color:green;'>✓</span> 10X größerer Markt als Deutschland  
                  <span style='color:green;'>✓</span> Höhere Margen durch Premium-Positionierung  
                  <span style='color:green;'>✓</span> Starke E-Commerce-Infrastruktur  
                  <span style='color:green;'>✓</span> Weniger gesättigter Wettbewerb
                
                </div>
                """,
                unsafe_allow_html=True
            )
        with st.container():
            st.markdown(
                f"""
                <div class='frame-box' style='min-height:{FRAME_MIN_HEIGHT};'>

                **<span style='color:red;'>10X</span> Potential**

                Im Weihnachtsgeschäft werden auf Amazon US 10- bis 15-mal mehr Heizwesten verkauft als auf Amazon DE im ganzen Jahr.  
                <a href='#' onclick="alert('Helium 10 Daten  verfügbar auf Anfrage\\nQuelle: '); return false;">Quelle</a>
                </div>
                """,
                unsafe_allow_html=True
            )
        with st.container():
            st.markdown(
                f"""
                <div class='frame-box' style='min-height:{FRAME_MIN_HEIGHT};'>

                **Bürokratie**

                US-Strukturen (Steuern, Import + Logistik) sind unternehmerfreundlicher als das deutsche System, mit niedrigeren laufenden Kosten  
                [Quelle](https://www.ifo.de/en/press-release/2024-11-14/bureaucracy-germany-costs-146-billion-euros-year-lost-economic-output)
                </div>
                """,
                unsafe_allow_html=True
            )

show()
