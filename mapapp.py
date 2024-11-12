import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.set_page_config(layout='wide')

st.title('European Countries Map')
df = pd.read_csv('europe.csv')

mean_lat = df['Latitude'].mean()
mean_lon = df['Longitude'].mean()

m=folium.Map(location=[mean_lat, mean_lon], zoom_start=4)

for i, row in df.iterrows():
    folium.Marker(
        location=[row["Latitude"], row["Longitude"]],
        tooltip=row["Country"],
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(m)


st_folium(m, width=1400)
