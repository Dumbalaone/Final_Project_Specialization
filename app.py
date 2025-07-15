
import streamlit as st
import pandas as pd
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium
import os

st.set_page_config(page_title="HWC Predictor", layout="centered")

# Check if data exists
if not os.path.exists("conflict_predictions.csv"):
    st.error("❌ 'conflict_predictions.csv' not found. Please add it to the root folder.")
    st.stop()

# Load data
df = pd.read_csv("conflict_predictions.csv")
df_conflict = df[df["predicted_conflict"] == 1]

st.title("🐘 Human-Wildlife Conflict Hotspots")
st.markdown("Predicted conflict locations for elephants, buffalo, leopards, and more in Kenya.")

st.subheader("Top Conflict Species")
st.dataframe(df_conflict["scientificName"].value_counts())

st.subheader("Conflict Map")
m = folium.Map(location=[-3.3, 38.5], zoom_start=7)
marker_cluster = MarkerCluster().add_to(m)

for _, row in df_conflict.iterrows():
    folium.Marker(
        location=[row["decimalLatitude"], row["decimalLongitude"]],
        popup=row["scientificName"]
    ).add_to(marker_cluster)

st_data = st_folium(m, width=700, height=500)
