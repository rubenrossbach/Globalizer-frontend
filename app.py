import app1
import app2
import home
import streamlit as st

st.set_page_config(
    page_title="Globalizer",
    page_icon="chart_with_upwards_trend",
    layout="wide",
    initial_sidebar_state="collapsed")

CSS = """
iframe {
    width: 100%;
    height: 700px;
}
"""

st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)

#st.set_page_config(layout='wide')
PAGES = {
"Home Page": home,
"Display centers on a map": app1,
"About the project": app2
}
st.sidebar.title('Globalizer')
selection = st.sidebar.radio("Select", list(PAGES.keys()))
page = PAGES[selection]
page.app()
