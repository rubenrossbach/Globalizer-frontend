import streamlit as st
import webbrowser
def app():
    st.markdown(
        "<h1 style='text-align: center; color: black;'>Globalizer</h1>",
        unsafe_allow_html=True)
    st.write('''
    For this project, we used databases from ...
    ''')
    st.markdown('## The Team:')


    ###Team members

    #Ruben
    st.markdown('Ruben Rossbach:')
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        urlrLink = 'https://www.streamlit.io/'
        if st.button("Ruben's LinkedIn (n/a)"):
            webbrowser.open_new_tab(urlrLink)
    with col2:
        urlrGH = 'https://github.com/rubenrossbach'
        if st.button("Ruben's Github"):
            webbrowser.open_new_tab(urlrGH)
    with col3:
        pass
    with col4:
        pass
    with col5:
        pass
    with col6:
        pass
    #Arvin
    st.markdown('Arvin Azimifard:')
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        urlaLink = 'https://www.linkedin.com/in/arvin-azimi-fard-85187717a/'
        if st.button("Arvin's LinkedIn"):
            webbrowser.open_new_tab(urlaLink)
    with col2:
        urlaGH = 'https://github.com/ArvinAzimifard'
        if st.button("Arvin's GitHub"):
            webbrowser.open_new_tab(urlaGH)
    with col3:
        pass
    with col4:
        pass
    with col5:
        pass
    with col6:
        pass
    #Martin
    st.markdown('Martin Reichardt:')
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        urlmLink = 'https://www.linkedin.com/in/martinreichardt/'
        if st.button("Martin's LinkedIn"):
            webbrowser.open_new_tab(urlmLink)
    with col2:
        urlmGH = 'https://github.com/reichardtma'
        if st.button("Martin's GitHub"):
            webbrowser.open_new_tab(urlmGH)
    with col3:
        pass
    with col4:
        pass
    with col5:
        pass
    with col6:
        pass
    #Pierre
    st.markdown('Pierre Sevenig:')
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        urlpLink = 'https://www.linkedin.com/in/pierre-sevenig-483140178/'
        if st.button("Pierre's LinkedIn"):
            webbrowser.open_new_tab(urlpLink)
    with col2:
        urlpGH = 'https://github.com/psevenig '
        if st.button("Pierre's GitHub"):
            webbrowser.open_new_tab(urlpGH)
    with col3:
        pass
    with col4:
        pass
    with col5:
        pass
    with col6:
        pass
    return
