# 🐘 Human-Wildlife Conflict Predictor (Streamlit App)

An interactive web app to visualize and explore predicted Human-Wildlife Conflict (HWC) hotspots in Southeastern Kenya — specifically focused on the counties of **Taita-Taveta, Kwale, and Kilifi**.

---

## 🌍 Live App

👉 [Click here to view the live app](https://finalprojectspecialization-ckztyr6d9bkkmjlwg8usy7.streamlit.app/)  


---

## 📦 About the App

This app uses a machine learning model to predict conflict-prone wildlife observations from GBIF data. It focuses on species known to cause conflict such as:

- 🐘 *Loxodonta africana* (African Elephant)
- 🐃 *Syncerus caffer* (African Buffalo)
- 🐒 *Papio cynocephalus* (Yellow Baboon)
- 🐗 *Potamochoerus larvatus* (Bush Pig)
- 🐆 *Panthera pardus* (Leopard)

Users can:
- View species involved in conflict
- Explore seasonal trends
- Interact with a conflict prediction map built using **Folium**

---

## 📁 File Structure

| File | Description |
|------|-------------|
| `app.py` | Main Streamlit app |
| `conflict_predictions.csv` | Model predictions with coordinates |
| `requirements.txt` | Python dependencies |
| `.gitignore` | Prevents venv and temp files from being committed |

---

# Data set obtained from : https://doi.org/10.15468/dl.wjkkeu

## 🚀 How to Run Locally

```bash
# Clone this repo
git clone https://github.com/Dumbalaone/Final_Project_Specialization.git
cd hwc-streamlit-app

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py


