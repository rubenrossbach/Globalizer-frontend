import streamlit as st
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
        st.button("Ruben's LinkedIn")
    with col2:
        st.button("Ruben's GitHub")
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
        st.button("Arvin's LinkedIn")
    with col2:
        st.button("Arvin's GitHub")
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
        st.button("Marin's LinkedIn")
    with col2:
        st.button("Martin's GitHub")
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
        st.button("Pierre's LinkedIn")
    with col2:
        st.button("Pierre's GitHub")
    with col3:
        pass
    with col4:
        pass
    with col5:
        pass
    with col6:
        pass
    return
