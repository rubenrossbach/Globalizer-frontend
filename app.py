import app1
import app2
import streamlit as st
st.set_page_config(layout='wide')
PAGES = {
"Display centers on a map": app1,
"Statistics about the country": app2
}
st.sidebar.title('Globalizer')
selection = st.sidebar.radio("Select", list(PAGES.keys()))
page = PAGES[selection]
page.app()
