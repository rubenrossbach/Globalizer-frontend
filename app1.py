
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


def app():
#Basic Layout stuff

    col1, col2 = st.columns(2)

#Get dropdown list for countries
    def get_country():
        return countries

    country = get_country()


    country_list = st.multiselect('Select countries', country)

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

            threshold = st.slider('Select mean distance to coustomer',10, 500)
            centers = None


    # transform country codes
    country_code_list = [trans[c] for c in country_list]
    country_code_string = ",".join(country_code_list)

#get coordinates
    base_url = 'https://globalizer-6mlwsep2ja-ey.a.run.app/predict/'
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
    })

#center the map
    center =[sum(i[0] for i in coordinate)/len(coordinate), sum(i[1] for i in coordinate)/len(coordinate)]


#display map
    col1, col2 = st.columns(2)
    with col1:
        m = folium.Map(location=center)


#display coordinates on map and style tooltip
    for i in range(len(df)):
        folium.Marker(coordinate[i], tooltip=df.loc[i,'Address']).add_to(m)


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


#Get Address to display on page
    st.write("# Your Centers")
    st.dataframe(df)
    return
