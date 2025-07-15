import streamlit as st
import pandas as pd
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium
import os
import matplotlib.pyplot as plt

st.set_page_config(page_title="HWC Predictor", layout="centered")

# Load dataset
if not os.path.exists("conflict_predictions.csv"):
    st.error("❌ 'conflict_predictions.csv' not found in the app folder.")
    st.stop()

df = pd.read_csv("conflict_predictions.csv")

# Filter only predicted conflict rows
df_conflict = df[df["predicted_conflict"] == 1].copy()

# Prepare date & month columns
df_conflict['eventDate'] = pd.to_datetime(df_conflict['eventDate'], errors='coerce')
df_conflict['month'] = df_conflict['eventDate'].dt.month

# Sidebar filter
st.sidebar.header("🔍 Filter")
species_list = df_conflict["scientificName"].unique()
selected_species = st.sidebar.multiselect("Choose species to display on the map:", species_list, default=species_list)

filtered_df = df_conflict[df_conflict["scientificName"].isin(selected_species)]

# Main header
st.title("🐘 Human-Wildlife Conflict Hotspots")
st.markdown("This app shows predicted conflict-prone wildlife sightings in Taita-Taveta, Kwale, and Kilifi counties.")

# Species frequency chart
st.subheader("📊 Conflict Counts by Species")
species_counts = df_conflict['scientificName'].value_counts()
fig1, ax1 = plt.subplots()
species_counts.plot(kind='bar', ax=ax1, color='teal')
ax1.set_ylabel("Sightings")
st.pyplot(fig1)

# Monthly trend chart
st.subheader("🕒 Monthly Conflict Trend")
monthly_counts = df_conflict['month'].value_counts().sort_index()
fig2, ax2 = plt.subplots()
monthly_counts.plot(kind='bar', ax=ax2, color='orange')
ax2.set_xlabel("Month")
ax2.set_ylabel("Number of Conflicts")
st.pyplot(fig2)

# Map display
st.subheader("🗺️ Conflict Hotspots Map")
m = folium.Map(location=[-3.3, 38.5], zoom_start=7)
marker_cluster = MarkerCluster().add_to(m)

for _, row in filtered_df.iterrows():
    folium.Marker(
        location=[row["decimalLatitude"], row["decimalLongitude"]],
        popup=row["scientificName"]
    ).add_to(marker_cluster)

st_data = st_folium(m, width=700, height=500)

# Footer
st.markdown("---")
st.markdown("**Data Source**: GBIF.org (14 July 2025) [DOI: 10.15468/dl.wjkkeu](https://doi.org/10.15468/dl.wjkkeu)")
