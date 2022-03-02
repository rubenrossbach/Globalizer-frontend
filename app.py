
import streamlit as st
import pandas as pd
import numpy as np
from countries import countries
import requests
import folium
from streamlit_folium import folium_static
from folium import plugins

#Basic Layout stuff
st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

#Get dropdown list for countries
def get_country():
    return countries

country = get_country()

with col1:
    st.multiselect('Select countries', country)

#Select number of clusters
with col2:
    st.number_input('Select a number of clusters', 1, 10000)

#select percentage of people to reach
st.slider('Percenage of people to reach',0, 100)



#data for coordinates
coordinate = [[51.14365216, 12.90129043],
       [49.9082329 ,  8.32919233],
       [48.51070336,  9.05212022],
       [49.95573197, 10.91326732],
       [53.75704471, 10.06461158],
       [51.17749919,  6.9799287 ],
       [51.94432852, 10.19479602],
       [52.47122199,  8.2674454 ],
       [52.72249955, 13.29947277],
       [48.34339277, 11.74843626]]

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
      responses.append(response['address'])
df = pd.DataFrame(responses)
df = df[['road', 'village', 'town', 'county', 'state', 'postcode', 'country']]
df = df.replace(np.nan, "Not Available")

#center the map
center =[sum(i[0] for i in coordinate)/len(coordinate), sum(i[1] for i in coordinate)/len(coordinate)]


#display map
m = folium.Map(location=center,

                )


#display coordinates on map and style tooltip
for i in range(len(df)):
  folium.Marker(coordinate[i], tooltip=f"""Road: {df.loc[i,'road']},
                                        Village: {df.loc[i,'village']},
                                        Town: {df.loc[i,'town']},
                                        County: {df.loc[i, 'county']}""").add_to(m)



#Google Maps
basemaps = {
    'Google Maps': folium.TileLayer(
        tiles = 'https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',
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


st.dataframe(df)
