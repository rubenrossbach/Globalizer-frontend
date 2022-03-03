import app1
import app2
import streamlit as st
PAGES = {
"Page 1": app1,
"Page 2": app2
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
