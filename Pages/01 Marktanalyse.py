import streamlit as st
import streamlit_echarts as st_echarts
import matplotlib.pyplot as plt

st.set_page_config(page_title="Marktanalyse", layout="wide")

def show():
    st.header("Deutschland vs. USA")

    # Split into two columns: left for buttons, right for table
    col_left, col_right = st.columns([1, 2])

    with col_left:
        highlight_10x = st.button("~10X Markt", key="markt10x")
        highlight_future = st.button("Zukunfts-Potential", key="future_potential")
        highlight_barriers = st.button("Marktbarrieren", key="marktbarrieren")

    # Custom CSS for highlights and gold USA column
    st.markdown(
        """
        <style>
        .markt-table {
            margin-left: auto;
            margin-right: auto;
        }
        .markt-table th, .markt-table td { padding: 8px 16px; text-align: center; font-size: 1.1em; }
        .markt-table th { background: #f5f5f5; }
        .markt-table .usa { color: #CFB53B; font-weight: bold; }
        .markt-table .highlight-blue { background: #d0ebff !important; }
        .markt-table .highlight-barrier { background: #ffe599 !important; font-weight: bold; }
        </style>
        """,
        unsafe_allow_html=True
    )

    with col_right:
        # Table HTML with optional highlights and extra column
        if highlight_10x:
            table_html = """
            <table class="markt-table">
                <tr>
                    <th>Kennzahl</th>
                    <th>Deutschland</th>
                    <th>USA</th>
                    <th>10X</th>
                </tr>
                <tr>
                    <td>Marktvolumen</td>
                    <td class="highlight-blue">€ 85 Mio.</td>
                    <td class="usa highlight-blue">$ 249 Mio.</td>
                    <td class="highlight-blue">x3</td>
                </tr>
                <tr>
                    <td>E-Commerce Anteil</td>
                    <td class="highlight-blue">15,2%</td>
                    <td class="usa highlight-blue">44,9%</td>
                    <td class="highlight-blue">x3</td>
                </tr>
                <tr>
                    <td>Wachstumsrate</td>
                    <td>3,1% CAGR</td>
                    <td class="usa">6,4% - 14,2% CAGR</td>
                    <td></td>
                </tr>
                <tr>
                    <td>Konkurrenzdichte</td>
                    <td>Hoch</td>
                    <td class="usa">Moderat</td>
                    <td></td>
                </tr>
                <tr>
                    <td>Regulierung</td>
                    <td>Sehr hoch</td>
                    <td class="usa">Moderat</td>
                    <td></td>
                </tr>
            </table>
            """
        elif highlight_future:
            table_html = """
            <table class="markt-table">
                <tr>
                    <th>Kennzahl</th>
                    <th>Deutschland</th>
                    <th>USA</th>
                    <th>Zukunft</th>
                </tr>
                <tr>
                    <td>Marktvolumen</td>
                    <td>€ 85 Mio.</td>
                    <td class="usa">$ 249 Mio.</td>
                    <td></td>
                </tr>
                <tr>
                    <td>E-Commerce Anteil</td>
                    <td>15,2%</td>
                    <td class="usa">44,9%</td>
                    <td></td>
                </tr>
                <tr>
                    <td>Wachstumsrate</td>
                    <td class="highlight-blue">3,1% CAGR</td>
                    <td class="usa highlight-blue">6,4% - 14,2% CAGR</td>
                    <td class="highlight-blue">x2 - x4</td>
                </tr>
                <tr>
                    <td>Konkurrenzdichte</td>
                    <td>Hoch</td>
                    <td class="usa">Moderat</td>
                    <td></td>
                </tr>
                <tr>
                    <td>Regulierung</td>
                    <td>Sehr hoch</td>
                    <td class="usa">Moderat</td>
                    <td></td>
                </tr>
            </table>
            """
        elif highlight_barriers:
            table_html = """
            <table class="markt-table">
                <tr>
                    <th>Kennzahl</th>
                    <th>Deutschland</th>
                    <th>USA</th>
                    <th>Barrieren</th>
                </tr>
                <tr>
                    <td>Marktvolumen</td>
                    <td>€ 85 Mio.</td>
                    <td class="usa">$ 249 Mio.</td>
                    <td></td>
                </tr>
                <tr>
                    <td>E-Commerce Anteil</td>
                    <td>15,2%</td>
                    <td class="usa">44,9%</td>
                    <td></td>
                </tr>
                <tr>
                    <td>Wachstumsrate</td>
                    <td>3,1% CAGR</td>
                    <td class="usa">6,4% - 14,2% CAGR</td>
                    <td></td>
                </tr>
                <tr>
                    <td>Konkurrenzdichte</td>
                    <td class="highlight-blue">Hoch</td>
                    <td class="usa highlight-blue">Moderat</td>
                    <td class="highlight-blue">Standortvorteil</td>
                </tr>
                <tr>
                    <td>Regulierung</td>
                    <td class="highlight-blue">Sehr hoch</td>
                    <td class="usa highlight-blue">Moderat</td>
                    <td class="highlight-blue">Standortvorteil</td>
                </tr>
            </table>
            """
        else:
            table_html = """
            <table class="markt-table">
                <tr>
                    <th>Kennzahl</th>
                    <th>Deutschland</th>
                    <th>USA</th>
                </tr>
                <tr>
                    <td>Marktvolumen</td>
                    <td>€ 85 Mio.</td>
                    <td class="usa">$ 249 Mio.</td>
                </tr>
                <tr>
                    <td>E-Commerce Anteil</td>
                    <td>15,2%</td>
                    <td class="usa">44,9%</td>
                </tr>
                <tr>
                    <td>Wachstumsrate</td>
                    <td>3,1% CAGR</td>
                    <td class="usa">6,4% - 14,2% CAGR</td>
                </tr>
                <tr>
                    <td>Konkurrenzdichte</td>
                    <td>Hoch</td>
                    <td class="usa">Moderat</td>
                </tr>
                <tr>
                    <td>Regulierung</td>
                    <td>Sehr hoch</td>
                    <td class="usa">Moderat</td>
                </tr>
            </table>
            """

        st.markdown(table_html, unsafe_allow_html=True)

        st.markdown(
            "<div style='text-align:center;'>"
            "Quellen: "
            "<a href='https://www.fortunebusinessinsights.com/heated-clothing-market-103861' target='_blank'>Fortune Business Insights</a>; "
            "<a href='https://www.theinsightpartners.com/de/reports/heated-clothing-market' target='_blank'>The Insight Partners</a>; "
            "<a href='https://www.marketresearchintellect.com/de/blog/powering-up-comfort-heated-jacket-market-grows-amid-demand-for-innovative-winter-wear/' target='_blank'>Market Research Intellect</a>"
            "</div>",
            unsafe_allow_html=True
        )

    # Grouped bar chart data
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    years = np.arange(2023, 2033)
    de_values = np.linspace(82, 108, len(years))
    usa_values = np.linspace(180, 332, len(years))

    df_grouped = pd.DataFrame({
        "Jahr": years,
        "Deutschland": de_values,
        "USA": usa_values
    })

    # Create grouped bar chart with Plotly (like the next module)
    import plotly.graph_objects as go

    fig = go.Figure(data=[
        go.Bar(name='Deutschland', x=years, y=de_values, marker_color='#1A2942'),
        go.Bar(name='USA', x=years, y=usa_values, marker_color="#CFB53B")
    ])
    fig.update_layout(
        barmode='group',
        xaxis_title='Jahr',
        yaxis_title='Marktvolumen (Mio.)',
        title='Marktvolumen-Entwicklung',
        legend_title_text='Land'
    )


    st.plotly_chart(fig, use_container_width=True)

        # Add subheader for the following section
    st.subheader("Zielgruppe")

    col1, col2 = st.columns(2)
    with col1:
        with st.container():
                st.markdown("<span style='font-size:1.1em; font-weight:400;'>Indoor-Produkte</span>", unsafe_allow_html=True)
                pie_option_indoor = {
                    "tooltip": {"trigger": "item"},
                    "series": [
                        {
                            "type": "pie",
                            "radius": ["50%", "70%"],
                            "avoidLabelOverlap": False,
                            "label": {"show": False, "position": "center"},
                            "emphasis": {
                                "label": {
                                    "show": True,
                                    "fontSize": "18",
                                    "fontWeight": "bold"
                                }
                            },
                            "data": [
                                {"value": 59, "name": "Weiblich", "itemStyle": {"color": "#FFB6C1"}},
                                {"value": 41, "name": "Männlich", "itemStyle": {"color": "#7EC8E3"}},
                            ],
                        }
                    ],
                }
                st_echarts.st_echarts(options=pie_option_indoor, height="220px")
                st.markdown(
                    """
                    <div style='display:flex; justify-content:center; gap:1.5em; margin-top:-1em;'>
                        <span style='font-size:0.95em; display:flex; align-items:center;'>
                            <span style='display:inline-block; width:14px; height:14px; border-radius:50%; background:#FFB6C1; margin-right:6px;'></span>
                            Weiblich
                        </span>
                        <span style='font-size:0.95em; display:flex; align-items:center;'>
                            <span style='display:inline-block; width:14px; height:14px; border-radius:50%; background:#7EC8E3; margin-right:6px;'></span>
                            Männlich
                        </span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                show_indoor_info = st.button("Warum sind 59 % der Indoor-Kunden weiblich?", key="indoor_info_btn")
                if show_indoor_info:
                    st.info(
                        "1. Frauen frieren nachweislich häufiger als Männer, besonders in Ruhe- oder Innenraumsituationen.\n"
                        "2. Frauen sind im privaten Konsum oft komfortorientierter – Stichwort: 'Cocooning-Trend'\n"
                        "3. Studien zeigen: Frauen dominieren bei Käufen im Bereich Home & Living, inklusive Wärmeanwendungen.\n"
                        "4. Viele Indoor-Heizprodukte werden auch als Geschenk für Frauen gekauft → weibliche Zielgruppe doppelt relevant (Käuferin & Beschenkte)."
                    )

        with col2:
            with st.container():
                st.markdown("<span style='font-size:1.1em; font-weight:400;'>Outdoor-Produkte</span>", unsafe_allow_html=True)
                pie_option_outdoor = {
                    "tooltip": {"trigger": "item"},
                "series": [
                    {
                        "type": "pie",
                        "radius": ["50%", "70%"],
                        "avoidLabelOverlap": False,
                        "label": {"show": False, "position": "center"},
                        "emphasis": {
                            "label": {
                                "show": True,
                                "fontSize": "18",
                                "fontWeight": "bold"
                            }
                        },
                        "labelLine": {"show": False},
                        "data": [
                            {"value": 44, "name": "Weiblich", "itemStyle": {"color": "#FFB6C1"}},
                            {"value": 56, "name": "Männlich", "itemStyle": {"color": "#7EC8E3"}},
                        ],
                    }
                ],
            }
            st_echarts.st_echarts(options=pie_option_outdoor, height="220px")
            st.markdown(
                """
                <div style='display:flex; justify-content:center; gap:1.5em; margin-top:-1em;'>
                    <span style='font-size:0.95em; display:flex; align-items:center;'>
                        <span style='display:inline-block; width:14px; height:14px; border-radius:50%; background:#FFB6C1; margin-right:6px;'></span>
                        Weiblich
                    </span>
                    <span style='font-size:0.95em; display:flex; align-items:center;'>
                        <span style='display:inline-block; width:14px; height:14px; border-radius:50%; background:#7EC8E3; margin-right:6px;'></span>
                        Männlich
                    </span>
                </div>
                """,
                unsafe_allow_html=True
            )
            show_outdoor_info = st.button("Warum sind 56 % der Outdoor-Kunden männlich?", key="outdoor_info_btn")
            if show_outdoor_info:
                st.info(
                    "1. Männer sind häufiger in Berufen oder Hobbies aktiv, bei denen sie sich längere Zeit draußen aufhalten.\n"
                    "2. Männer bevorzugen häufiger technische Gadgets, und sehen Heizkleidung eher als Tool oder 'Gear' denn als Lifestyle-Produkt.\n"
                    "3. Besonders im Outdoor-Segment (z. B. Jagd) ist die Zahlungsbereitschaft für hochwertige Ausrüstung unter Männern deutlich höher.\n"
                    "4. Viele Top-Heizjacken & Westen (Milwaukee, Bosch) zeigen in ihren Rezensionen/UGC einen starken Männeranteil → Die Daten spiegeln das Konsumverhalten direkt wider."
                )

    st.write("")
    colA, colB = st.columns(2)
    FRAME_MIN_HEIGHT = "220px"  # Adjust as needed for your content

    # Key info with eyecatcher
    st.markdown(
        """
        <div style='display:flex; align-items:center; margin-top:18px;'>
            <span style='font-size:1.8em; color:#CFB53B; margin-right:12px;'>&#9733;</span>
            <span style='font-style:italic; font-size:1.35em; font-weight:bold;'>
                Der Markt ist da. Was fehlt, ist eine starke Marke mit Vertrauen, Qualität und US kompatibler Positionierung.
            </span>
        </div>
        """,
        unsafe_allow_html=True
    )

show()