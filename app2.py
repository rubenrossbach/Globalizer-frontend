import streamlit as st
import webbrowser

def app():


    st.markdown("""
        <h1 style='text-align: justify; color: black;'>Globalizer</h1>

        """,unsafe_allow_html=True)
    st.markdown("""
                ## The Team:
                We are a group of graduates of the Le Wagon Data Science bootcamp. <br>
                **Globalizer** is our final project that combines all of the skills we
                have learned during the bootcamp: Data analysis with Python, Machine Learning, SQL,
                data visualization, building a cloud backend on Google Cloud, creating our own API, and designing a
                frontend website. <br>
                If you would like to get in contact, feel free to reach out via LinkedIn.
                """, unsafe_allow_html=True)


    ###Team members

    #Ruben
    st.markdown("""
        <p style='text-align: center; color: black;'>Ruben Rossbach</p>

        """,unsafe_allow_html=True)
    col1, col2, col3, col4, col5, col6, col7, col8, col9= st.columns(9)
    with col5:
        st.image('https://avatars.githubusercontent.com/u/96783837?v=4', width=110)
    st.markdown("Studied Chemical Engineering (M.Sc.) at TUM. I always liked the computational aspects of my study projects and decided the Data Science bootcamp is right for me. I wanted to unlock the power of data to solve real world problems and learn to build usable products. Managing this project required not just a lot of coding, but also project management and communication. I am looking forward to using these new skills for the next project.")
    col1, col2, col3, col4, col5, col6, col7= st.columns(7)
    with col3:
        urlrLink = "[Ruben's LinkedIn](https://www.linkedin.com/in/ruben-rossbach/)"
        st.markdown(urlrLink, unsafe_allow_html=True)
    with col5:
        urlrGH = "[Ruben's Github](https://github.com/rubenrossbach)"
        st.markdown(urlrGH, unsafe_allow_html=True)

    #Arvin
    st.markdown("""
        <p style='text-align: center; color: black;'>Arvin Azimifard</p>

        """,unsafe_allow_html=True)
    col1, col2, col3, col4, col5, col6, col7, col8, col9= st.columns(9)
    with col5:
        st.image('https://avatars.githubusercontent.com/u/97016313?v=4', width=110)
    st.markdown("Born and raised in Frankfurt. After High school, I started studying chemical engineering due to my strength in sciences. Besides the university, I launched a Sales - Startup, and as it grew and things got more serious due to responsibility for my employees, I decided to pause my studies and go All-in with the business. During that time I attended many psychological seminars to improve the sales results and got hooked by the human brain. So after 2 years of blood, sweat, and tears, I have become rich - no just kidding I failed hard.. I decided to continue to follow my curiosity about psychology and started studying Business Psychology and Business Administration in Frankfurt. Since then I gathered some work experience trough internships and a Trainee position - but I felt that something is missing. My analytical part of me was not satisfied, and I missed solving problems through thinking like it was earlier before in the sciences. So I did some research, what kind of jobs could fit my needs more. And there it was: Data Science. So I talked to people, who already worked in this field or doing a doctorate in Data Science, and I understand, that I could really prosper in this field due to my hybrid personality (50 % nerd, 50 % social guy). Since then I finished a Python course on Udemy and currently I am doing the Data Science certificate from IBM. I am really excited about what I will experience at le wagon. My goals are a) to get a better big picture of Data Science b) have a better feeling in which area i want to work c) get a job, where I can use the learnings and help with my knowledge.")
    col1, col2, col3, col4, col5, col6, col7= st.columns(7)
    with col3:
        urlaLink = "[Arvin's LinkedIn](https://www.linkedin.com/in/arvin-azimi-fard-85187717a/)"
        st.markdown(urlaLink, unsafe_allow_html=True)
    with col5:
        urlaGH = "[Arvin's Github](https://github.com/ArvinAzimifard)"
        st.markdown(urlaGH, unsafe_allow_html=True)

    #Martin
    st.markdown("""
        <p style='text-align: center; color: black;'>Martin Reichardt</p>

        """,unsafe_allow_html=True)
    col1, col2, col3, col4, col5, col6, col7, col8, col9= st.columns(9)
    with col5:
        st.image('https://res.cloudinary.com/wagon/image/upload/c_fill,g_face,h_200,w_200/v1644222327/cjsc5fl2ayoarslqey6w.jpg', width=110)
    st.markdown("Being a social scientist, in the past I have worked mostly with qualitative data, such as interviews, focus groups and participatory observations. Fairly recently, I have started to really dive into quantitative data as more and more of large datasets are being made available freely on the web. I am very excited and curious to learn new ways how to work with datasets and learn how to implement machine learning models.")
    col1, col2, col3, col4, col5, col6, col7= st.columns(7)
    with col3:
        urlmLink = "[Martin's LinkedIn](https://www.linkedin.com/in/martinreichardt/)"
        st.markdown(urlmLink, unsafe_allow_html=True)
    with col5:
        urlmGH = "[Martin's Github](https://github.com/reichardtma)"
        st.markdown(urlmGH, unsafe_allow_html=True)

    #Pierre
    st.markdown("""
        <p style='text-align: center; color: black;'>Pierre Sevenig</p>

        """,unsafe_allow_html=True)
    col1, col2, col3, col4, col5, col6, col7, col8, col9= st.columns(9)
    with col5:
        st.image('https://res.cloudinary.com/wagon/image/upload/c_fill,g_face,h_200,w_200/v1643799861/qfymwplp5pbowrpjmajy.jpg', width=110)
    st.markdown("Hey, I am Pierre from Luxembourg and I love doing sports and all kind of outdoor activities. I recently finished my bachelor's degree in scientific economics and I am going to start my master's in Innsbruck. In the meantime i am trying to master my coding skills by joining Le Wagon Munich and I am continuing to work on data science related projects even after the bootcamp.")
    col1, col2, col3, col4, col5, col6, col7= st.columns(7)
    with col3:
        urlpLink = "[Pierre's LinkedIn](https://www.linkedin.com/in/pierre-sevenig-483140178/)"
        st.markdown(urlpLink, unsafe_allow_html=True)

    with col5:
        urlpGH = "[Pierre's GitHub](https://github.com/psevenig)"
        st.markdown(urlpGH, unsafe_allow_html=True)

    return
