
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
    #st.set_page_config(layout='wide')

    col1, col2, col3 = st.columns(3)

#Get dropdown list for countries
    def get_country():
        return countries

    country = get_country()

    with col1:
        country_list = st.multiselect('Select countries', country)

#Select number of clusters
    with col2:
        centers = st.number_input('Select a number of clusters', 1, 10000)

#mean distance
    with col3:
        threshold = st.slider('Select mean distance to coustomer',10, 500)

#select percentage of people to reach
    #st.slider('Percentage of people to reach',0, 100)

    # transform country codes
    country_code_list = [trans[c] for c in country_list]
    country_code_string = ",".join(country_code_list)


#get coordinates
    base_url = 'http://127.0.0.1:8000/predict'
    params = {
        'country': country_code_string,
        'threshold': threshold,
        'n_centers': centers
    }
    response1 = requests.get(base_url, params = params).json()
    coordinate = response1['centers']

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
    m = folium.Map(location=center,

                )


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
    basemaps['Esri Satellite'].add_to(m)
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
