import streamlit as st
from streamlit_lottie import st_lottie
import requests

# --- Configuration de la page ---
st.set_page_config(
    page_title="À propos - Taxi NYC Dashboard",
    page_icon="ℹ️",
    layout="centered"
)

# --- Titre principal ---
st.markdown(
    """
    <h1 style='text-align:center; color:#2E86C1;'>ℹ️ À propos</h1>
    <p style='text-align:center; font-size:1.1em;'>
    Découvrez le projet, ses objectifs et l'auteur.
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

# --- Animation Lottie ---
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url = "https://assets10.lottiefiles.com/packages/lf20_u4yrau.json"  # exemple animation taxi
lottie_json = load_lottie_url(lottie_url)

st_lottie(lottie_json, height=250, key="taxi_animation")

# --- Section : Description du projet ---
st.subheader("📌 Description du projet")
st.markdown(
    """
    Ce dashboard interactif a été développé pour analyser et prédire le montant total
    des courses de taxi à New York. Il inclut :
    - Un **pipeline ETL** pour nettoyer et transformer les données.
    - Des **analyses exploratoires** avec visualisations interactives.
    - Un **modèle de prédiction** (Random Forest) pour estimer les montants.
    
    L'objectif est de fournir un outil clair et intuitif pour l'analyse des données TLC.
    """
)

# --- Section : Objectifs ---
st.subheader("🎯 Objectifs")
st.markdown(
    """
    - Visualiser les tendances mensuelles et la distribution des courses.
    - Explorer les comportements des passagers et les types de paiement.
    - Prédire rapidement le montant d'une course en fonction de ses caractéristiques.
    - Fournir une interface intuitive et interactive pour les utilisateurs.
    """
)

# --- Section : Auteur avec photo ---
st.subheader("👤 Auteur")
col1, col2 = st.columns([1, 3])
with col1:
    st.image("https://raw.githubusercontent.com/kaderkouadio/Fullstacks_Analytics_Pipelines2/main/App_streamlit/Images/profil.jpg", width=120)
with col2:
    st.markdown(
    """
    <div style="text-align: center; line-height: 1.6;">
        <h2>👋 À propos de moi</h2>
        <p><strong>KOUADIO KADER</strong></p>
        <p>Économiste | Analyste Financier | Data Analyst | Développeur BI & Intelligence Artificielle<br>
        Passionné par l'analyse de données et les dashboards interactifs</p>
        <p>
            <a href="https://www.linkedin.com/in/koukou-kader-kouadio-2a32371a4/" target="_blank">🔗 LinkedIn</a> |
            <a href="mailto:kkaderkouadio@gmail.com">📧 Email</a>
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Section : Sources de données ---
st.subheader("🗂 Sources de données")
st.markdown(
    """
    - [TLC Trip Data NYC](https://www.nyc.gov/site/tlc/about/about-tlc.page) : Données publiques sur les courses de taxi et limousine.
    - Données transformées et stockées via **SQLite** pour l'analyse et la prédiction.
    """
)

# --- Section : Remerciements ---
st.subheader("🙏 Remerciements")
st.markdown(
    """
    Merci à tous ceux qui ont contribué à la collecte et à la maintenance des données TLC,
    et à la communauté Streamlit pour les outils interactifs.
    """
)
