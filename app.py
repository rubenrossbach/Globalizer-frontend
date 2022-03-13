import app1
import app2
import streamlit as st

st.set_page_config(
    page_title="Globalizer",
    page_icon="https://freesvg.org/img/1386749018.png",
    layout="wide",
    initial_sidebar_state="expanded")

CSS = """
iframe {
    width: 100%
}
img {
    display: block;
    margin-left: center;
    margin-right: center;
    width: 50%;
    border-radius: 50%;
}

"""

st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)

PAGES = {
"Home": app1,
"About": app2
}

st.sidebar.title('Globalizer')

selection = st.sidebar.radio("Select", list(PAGES.keys()))
page = PAGES[selection]
page.app()
