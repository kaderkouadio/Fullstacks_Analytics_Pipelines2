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
pages = {
    "🏠 Home": "App_streamlit/App.py",                        # Page d'accueil / présentation du projet
    "👤 A propos": "App_streamlit/page1.py",                  # Visualisations générales et pipeline
    "📊 Analyse exploratoire": "App_streamlit/page2.py",      # Analyse des données détaillée
    "🔎 Prédiction": "App_streamlit/page3.py"                 # Formulaire de prédiction taxi
}

# Barre latérale pour la navigation
st.sidebar.title("📌 Navigation")
selection = st.sidebar.radio("Aller à :", list(pages.keys()))

# Chargement de la page sélectionnée
page_file = pages[selection]
if os.path.exists(page_file):
    with open(page_file, "r", encoding="utf-8") as f:
        code = f.read()
        exec(code, globals())
else:
    st.error(f"❌ Fichier {page_file} introuvable")


