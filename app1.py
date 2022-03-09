
import streamlit as st
import pandas as pd
import numpy as np
from countries import countries, trans
import requests
import folium
from streamlit_folium import folium_static
from folium import plugins
from folium.plugins import HeatMap
from folium.plugins import HeatMapWithTime
from country_statistics import show_country_statistics


def app():
    st.markdown(
        "<h1 style='text-align: center; color: black;'>Globalizer</h1>",
        unsafe_allow_html=True)


    st.write(
        """
        Find the optimal locations for you warehouses, data centers or offices.
        Simply enter a country and let us do the magic.


        """
    )

    #Get dropdown list for countries
    def get_country():
        return countries

    country = get_country()
    country_list = st.multiselect('Choose one or more countries:', country)

    st.markdown('Choose one of these options:')
    col1, col2 = st.columns(2)

    # explanation
    st.markdown(
        """
        <details>
            <summary>Explanation</summary>
            You have several options to get the optimal locations for your needs:
            <ul>
                <li><strong>Number of centers </strong><br>
                You already know how many centers you want to open? Give this
                number to our algorithm and you will receive the optimal
                locations. This is applicable if you have a fixed budget for a
                certain number of centers and simply want to get the best
                locations for these.<br>
                Example: Choose <u>10</u> if you want 10 centers.</li>
                <li><strong>Mean distance </strong><br>
                You don't know yet how many centers to open, but distance is
                the deciding factor? Let us choose the optimal number of
                centers for you based on the average distance to the country's
                population.<br>
                Example: The average person in the country should not have
                to travel more than 50 km to get to their nearest center.
                Choose a mean distance of <u>50 km</u> in this case.</li>
                <li><strong>Radius and Population </strong><br>
                Each of your centers has an effective area it can cover. For
                example, you can limit the effective radius of your
                centers to 50 km. <br>
                Choose how many people should be inside the coverage area of
                your centers. Our algorithm will then determine the required
                number of centers and their optimal locations. You can choose
                population as a percentage from 0 to 100 % of the country's total.<br>
                Example: You want 60 % of the country's population to be within
                50 km of your centers. Choose <u>50 km</u> radius and <u>60 %</u>
                of the population.</li>
            </ul>
        </details>
        """,
        unsafe_allow_html=True
    )

    #Select buttons for mean distance/number of clusters

    if "current" not in st.session_state:

        st.session_state.current = None

    if "AAA" not in st.session_state:

        st.session_state.AAA = False

    if "BBB" not in st.session_state:

        st.session_state.BBB = False

    with col1:
        A = st.button("Select number of centers")

    with col2:
        B = st.button("Select mean distance to customer")


    if A:

        st.session_state.current = "A"


    if B:

        st.session_state.current = "B"

    if st.session_state.current != None:

        if st.session_state.current == "A":

            st.session_state.AAA = True

            st.session_state.BBB = False

            centers = st.number_input('Select a number of centers', 1, 10000)
            threshold = None
        else:

            st.session_state.BBB = True

            st.session_state.AAA = False

            threshold = st.slider('Select mean distance to coustomer in km',10, 500)
            centers = None


    # transform country codes
    country_code_list = [trans[c] for c in country_list]
    country_code_string = ",".join(country_code_list)

    # button to run
    col1, col2, col3 , col4, col5 , col6= st.columns(6)

    with col1:
        pass
    with col2:
        pass
    with col3:
        pass
    with col5:
        pass
    with col6:
        pass
    with col4 :
        ## chenge color of button
        c = st.markdown("""
        <style>
        div.stButton > button:first-child {
            background-color: #f23a3a;
            color:#ffffff;
        }
        </style>""", unsafe_allow_html=True)
        ##
        run_button = False
        if (st.session_state.current == "A" or st.session_state.current == "B") \
            and country_code_list != []:
            run_button = st.button('Run')


    if run_button:

        #get coordinates
        base_url = 'https://globalizer-2chu5w4mva-ey.a.run.app/predict'
        params = {
                'country': country_code_string,
                'threshold': threshold,
                'n_centers': centers
            }
        response1 = requests.get(base_url, params = params)
        st.write(response1.status_code)
        if response1.status_code == 500:
            coordinate = [
        [48.51070336,  9.05212022],
        [49.95573197, 10.91326732],
        [53.75704471, 10.06461158],
        [51.17749919,  6.9799287 ],
        [51.94432852, 10.19479602],
        [52.47122199,  8.2674454 ],
        [52.72249955, 13.29947277],
        [48.34339277, 11.74843626]]
            st.write('Internal server erros, using hardcoded coordinates instead.')

        else:
            #response1 = response1.json()
            coordinate = response1.json()["centers"]
        avg_distance = response1.json()["avg_distance"]
        st.write(f'Average distance: {round(avg_distance, 2)} km')
        #Get Dataframe
        url = 'https://nominatim.openstreetmap.org/reverse'
        responses=[]
        for coordinates in coordinate:

            lat = coordinates[0]
            lon = coordinates[1]
            params = {
                    'lat': lat,
                    'lon': lon,
                    'format': 'json'
                }
            response = requests.get(url, params = params).json()
            responses.append(response['display_name'])
        df = pd.DataFrame({
            "Address": responses,
            "Coordinates": coordinate
        }, index=list(range(1, (len(coordinate)+1))))

        #center the map
        center =[sum(i[0] for i in coordinate)/len(coordinate), sum(i[1] for i in coordinate)/len(coordinate)]


        #display map
        col1, col2 = st.columns(2)
        with col1:
            m = folium.Map(location=center)


        #display coordinates on map and style tooltip
        for i in range(len(df)):
            folium.Marker(coordinate[i], tooltip=df.loc[i+1,'Address']).add_to(m)


        #Google Maps
        basemaps = {
            'Google Maps': folium.TileLayer(
                tiles = 'https://mt1.google.com/vt/lyrs=h&x={x}&y={y}&z={z}',
                attr = 'Google',
                name = 'Google Maps',
                overlay = True,
                control = True
            ),
            'Google Satellite': folium.TileLayer(
                tiles = 'https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',
                attr = 'Google',
                name = 'Google Satellite',
                overlay = True,
                control = True
            ),
            'Google Terrain': folium.TileLayer(
                tiles = 'https://mt1.google.com/vt/lyrs=p&x={x}&y={y}&z={z}',
                attr = 'Google',
                name = 'Google Terrain',
                overlay = True,
                control = True
            ),
            'Google Satellite Hybrid': folium.TileLayer(
                tiles = 'https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}',
                attr = 'Google',
                name = 'Google Satellite',
                overlay = True,
                control = True
            ),
            'Esri Satellite': folium.TileLayer(
                tiles = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
                attr = 'Esri',
                name = 'Esri Satellite',
                overlay = True,
                control = True
            )
        }

        ##Data for heatmap
        #df_heat = df_small.drop(['Centers'], axis=1)
        #df_heat = df_heat.to_numpy()
        #HeatMap(df_heat).add_to(m)


        # Add custom basemaps

        basemaps['Google Maps'].add_to(m)
        basemaps['Google Satellite Hybrid'].add_to(m)
        basemaps['Google Terrain'].add_to(m)
        folium.LayerControl().add_to(m)




        #Plugins

        plugins.Fullscreen().add_to(m)
        plugins.LocateControl().add_to(m)
        plugins.MeasureControl(position='topright', primary_length_unit='kilometers', secondary_length_unit='miles', primary_area_unit='sqmeters', secondary_area_unit='acres').add_to(m)
        minimap = plugins.MiniMap()
        m.add_child(minimap)

        #####


        #automatic zoom start

        sw = min(coordinate)[0], min(coordinate)[1]
        ne = max(coordinate)[0], max(coordinate)[1]

        m.fit_bounds([sw, ne])




        # call to render Folium map in Streamlit

        folium_static(m)

        st.markdown('## Statistics about the country:')
        st.dataframe(show_country_statistics(country_code_list[0]))

        #Get Address to display on page
        st.write("## Your Centers:")
        st.dataframe(df)
        csv = df.to_csv()
        st.download_button(label = 'Download as CSV file', data = csv, file_name = 'centers.csv')


    # no button pressed
    else:
        #Setting up the world countries data URL
        # url = 'https://raw.githubusercontent.com/python-visualization/folium/master/examples/data'
        # country_shapes = f'{url}/world-countries.json'
        # basemaps = {
        #     'Google Maps': folium.TileLayer(
        #         tiles = 'https://mt1.google.com/vt/lyrs=h&x={x}&y={y}&z={z}',
        #         attr = 'Google',
        #         name = 'Google Maps',
        #         overlay = True,
        #         control = True
        #     )
        # }
        m = folium.Map() #location=[0,0], zoom_start=2.5)
        # folium.Choropleth(
        # #The GeoJSON data to represent the world country
        # geo_data=country_shapes,
        # # name='choropleth COVID-19',
        # # data=df_covid,
        # #The column aceppting list with 2 value; The country name and  the numerical value
        # # columns=['Country', 'Total Case'],
        # # key_on='feature.properties.name',
        # fill_color='blue',
        # # nan_fill_color='white'
        # ).add_to(m)
        m.fit_bounds([[-50,  -30],[70,60]])
        # basemaps['Google Maps'].add_to(m)
        folium_static(m)


    return
