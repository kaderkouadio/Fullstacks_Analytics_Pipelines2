###############################################
import os
import streamlit as st

# ---------------------------
# Configuration de la page
# ---------------------------

st.set_page_config(
    page_title="Fullstacks Analytics Pipelines",
    page_icon="🚀",
    layout="wide"
)

# ---------------------------
# Navigation Multi-pages
# ---------------------------

# Définition des pages avec icônes
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Pages disponibles (fichiers dans App_streamlit/)
pages = {
    "🏠 Home": "App.py",
    "👤 À propos": "page1.py",
    "📊 Analyse exploratoire": "page2.py",
    "🔎 Prédiction": "page3.py"
}

st.sidebar.title("📌 Navigation")
selection = st.sidebar.radio("Aller à :", list(pages.keys()))

# Construction du chemin exact
page_file = os.path.join(BASE_DIR, pages[selection])

if os.path.exists(page_file):
    with open(page_file, "r", encoding="utf-8") as f:
        exec(f.read(), globals())
else:
    st.error(f"❌ Fichier {page_file} introuvable")



