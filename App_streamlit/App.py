import streamlit as st

# Configuration de la page
st.set_page_config(
    layout="wide",
    page_title="Fullstacks Analytics Pipelines",
    page_icon="📊",
)

# Titre principal avec gradient
html_temp = """
    <div style="
        background: linear-gradient(90deg, #006400, #228B22); 
        padding:15px; 
        border-radius:15px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    ">
        <h1 style="color: white; text-align:center; font-size: 36px; margin:0;">
            🚖 Dashboard Fullstacks Analytics Pipelines
        </h1>
    </div>
    <p style="
        font-size: 20px; 
        font-weight: bold; 
        text-align:center; 
        margin-top:15px;
    ">
        Analyse des données Taxi 🚕 | Pipeline ELT complet ⚙️ | Visualisation interactive 📊
    </p>
"""
st.markdown(html_temp, unsafe_allow_html=True)

# Colonnes : profil | titre | LinkedIn
col1, col2, col3 = st.columns([1, 4, 1])

with col1:
    st.markdown(
        """
        <div style="display: flex; justify-content: center; align-items: center; height:100%;">
            <img src="https://raw.githubusercontent.com/kaderkouadio/Fullstacks_Analytics_Pipelines2/main/App_streamlit/Images/profil.jpg" 
                 width="80" 
                 style="border-radius:50%; border:2px solid white; box-shadow:0px 2px 5px rgba(0,0,0,0.3);"/>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <h2 style='text-align: center; margin: 0;'>🚖 Analyse et Prédiction des Courses de Taxi</h2>
        <p style='text-align: center; margin-top: 0.2em; font-size:1.05em;'>
            Pipeline complet ETL, transformation des données, analyse exploratoire et prédiction du montant total.
        </p>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        """
        <div style='display:flex; justify-content:flex-end; align-items:center; height:100%;'>
            <a href="https://www.linkedin.com/in/koukou-kader-kouadio-2a32371a4/" 
               target="_blank" 
               style='text-decoration: none; color: #0077b5; font-weight:bold; font-size:1.05em;'>
                👨‍💻 KOUADIO KADER
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.write(" ")

st.write(" ")

# =======================
# Phase 1 : Pipeline ELT
# =======================
st.markdown(
    """
    <h2 style='text-align: center; color: #4CAF50;'>Phase 1 : <strong>Pipeline ELT & Préparation des données</strong></h2>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns([2, 1])
with col1:
    st.image("https://raw.githubusercontent.com/kaderkouadio/Fullstacks_Analytics_Pipelines2/main/App_streamlit/Images/pipeline.png", width=600)

st.markdown(
    """
    <div style='text-align: justify; font-size: 16px; padding: 10px 30px;'>
        Cette phase consiste à construire un pipeline ELT complet pour :
        <ul>
            <li>Charger et nettoyer les données brutes (Parquet)</li>
            <li>Stocker les données transformées dans SQLite</li>
            <li>Créer des vues SQL pour faciliter l'analyse</li>
        </ul>
        Le pipeline est robuste, automatisé et prêt pour l'intégration dans l'application Streamlit.
    </div>
    """,
    unsafe_allow_html=True
)
with col2:
    st.markdown(
    """
    <div style='
        border: 2px solid #1f77b4; 
        padding: 0.5em; 
        border-radius: 6px; 
        text-align: center; 
        margin-bottom: 0.8em;
    '>
        <h1 style='margin-bottom: 0.2em;'>🚖 Exploration des Données Taxi & Limousine Commission (TLC)</h1>
    </div>
    <p style='text-align: center; font-size: 1.1em; margin-top: 0; margin-bottom: 0.5em;'>
        Analyse des courses de taxi à New York : montants, distances, types de paiement et tendances.
    </p>
    <p style='text-align: center;'>
        <a href='https://www.nyc.gov/site/tlc/about/about-tlc.page' target='_blank' style='color: #1f77b4; text-decoration: none;'>
            🔗 Accéder au site officiel de la TLC
        </a>
    </p>
    """,
    unsafe_allow_html=True
)

# =======================
# Phase 2 : Analyse Exploratoire
# =======================
st.markdown(
    """
    <h2 style='text-align: center; color: #4CAF50;'>Phase 2 : <strong>Analyse Exploratoire & Visualisation</strong></h2>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns([2, 1])
with col1:
    st.image("https://raw.githubusercontent.com/kaderkouadio/Fullstacks_Analytics_Pipelines2/main/App_streamlit/Images/visualisation.jpeg", width=600)

st.markdown(
    """
    <div style='text-align: justify; font-size: 16px; padding: 10px 30px;'>
        Cette phase se concentre sur l’exploration des données transformées :
        <ul>
            <li>Analyse des tendances mensuelles et répartition des trajets</li>
            <li>Distribution du nombre de passagers et analyse par type de paiement</li>
            <li>Visualisations interactives avec Plotly et Streamlit</li>
        </ul>
        L'objectif est de fournir des insights exploitables et des dashboards dynamiques.
    </div>
    """,
    unsafe_allow_html=True
)
with col2:
    st.markdown(
    """
    <div style='
        border: 3px solid #1f77b4; 
        border-radius: 8px; 
        padding: 12px; 
        text-align: center; 
        margin-bottom: 0.5em;
    '>
        <h1 style='margin: 0;'>📊 Analyse Exploratoire & Visualisation</h1>
    </div>
    <p style='text-align: center; font-size: 1.1em; margin-top: 0.5em; margin-bottom: 0.5em;'>
        Explorez les tendances, la répartition des trajets, les comportements des passagers 
        et les méthodes de paiement grâce à des visualisations interactives.
    </p>
    """,
    unsafe_allow_html=True
)

# =======================
# Phase 3 : Modèle de Prédiction & Application Streamlit #4CAF50
# =======================
st.markdown(
    """
    <h2 style='text-align: center; color: #4CAF50;'>Phase 3 : <strong>Développement du Modèle de Prédiction & Application Streamlit</strong></h2>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns([2, 1])
with col1:
    st.image("https://raw.githubusercontent.com/kaderkouadio/Fullstacks_Analytics_Pipelines2/main/App_streamlit/Images/streamlit3.jpeg", width=600)

st.markdown(
    """
    <div style='text-align: justify; font-size: 16px; padding: 10px 30px;'>
        Cette phase finalise le projet avec :
        <ul>
            <li>Entraînement d’un modèle <strong>Random Forest</strong> pour prédire le montant total d'une course</li>
            <li>Évaluation des performances du modèle et optimisation</li>
            <li>Déploiement dans une application <strong>Streamlit</strong> permettant aux utilisateurs d’effectuer des prédictions en direct</li>
        </ul>
        L’utilisateur saisit les caractéristiques d’une course et obtient instantanément une estimation du prix.
    </div>
    """,
    unsafe_allow_html=True
)
with col2:
   st.markdown(
    """
    <div style='
        border: 3px solid #1f77b4; 
        border-radius: 8px; 
        padding: 12px; 
        text-align: center; 
        margin-bottom: 0.5em;
    '>
        <h1 style='margin: 0;'>🔎 Prédiction en Direct</h1>
    </div>
    <p style='text-align: center; font-size: 1.1em; margin-top: 0.5em; margin-bottom: 0.5em;'>
        Simulez une course et obtenez le tarif estimé grâce au modèle d’apprentissage automatique.
    </p>
    """,
    unsafe_allow_html=True
)



# =======================
# Boîte d'information
# =======================
st.markdown(
    """
    <div style='
        margin-top: 30px;
        background-color: #e8f4fd;
        border-left: 5px solid #2196F3;
        padding: 15px 20px;
        border-radius: 5px;
        font-size: 16px;
        color: #333;
    '>
        ℹ️ <strong>Note :</strong> Le pipeline ELT peut prendre quelques secondes lors du premier chargement des fichiers Parquet.
    </div>
    """,
    unsafe_allow_html=True
)
