# streamlit_app.py
import streamlit as st
import folium
from streamlit_folium import st_folium

st.title("Top 10 Tourist Attractions in Seoul Loved by Foreigners")

# Sample data: name and coordinates
locations = [
    ("Gyeongbokgung Palace", 37.579617, 126.977041),
    ("Bukchon Hanok Village", 37.582604, 126.983998),
    ("Myeongdong Shopping Street", 37.563757, 126.982669),
    ("N Seoul Tower", 37.551169, 126.988227),
    ("Insadong", 37.574026, 126.985486),
    ("Hongdae", 37.557192, 126.923863),
    ("Lotte World", 37.511000, 127.098000),
    ("Changdeokgung Palace", 37.579438, 126.991046),
    ("COEX Mall", 37.512620, 127.059140),
    ("Dongdaemun Design Plaza", 37.566610, 127.009170)
]

# Create map
m = folium.Map(location=[37.5665, 126.9780], zoom_start=12)

for name, lat, lon in locations:
    folium.Marker([lat, lon], popup=name).add_to(m)

# Display map
st_folium(m, width=700, height=500)

# requirements.txt content would be in separate file
