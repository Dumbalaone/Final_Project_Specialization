import streamlit as st
import pandas as pd
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium

# Load data
df = pd.read_csv("conflict_predictions.csv")

st.title("🐘 Human-Wildlife Conflict Prediction")
st.markdown("Visualizing predicted conflict hotspots in Southeastern Kenya (Taita-Taveta, Kwale, Kilifi)")

# Filter for conflict predictions
df_pred = df[df["predicted_conflict"] == 1]

st.subheader("Conflict-Prone Species")
st.write(df_pred["scientificName"].value_counts())

st.subheader("Interactive Map of Predicted Conflict Hotspots")
# Create Folium map
m = folium.Map(location=[-3.3, 38.5], zoom_start=7)
marker_cluster = MarkerCluster().add_to(m)

for _, row in df_pred.iterrows():
    folium.Marker(
        location=[row["decimalLatitude"], row["decimalLongitude"]],
        popup=row["scientificName"]
    ).add_to(marker_cluster)

# Render Folium map in Streamlit
st_folium(m, width=700, height=500)
