import streamlit as st
import joblib
import pandas as pd
import os
from pathlib import Path
import re


# === Configuration et chargement des fichiers ===
# -------------------------
# ⚙️ Chargement du modèle
# -------------------------
MODEL_PATH = os.path.join("..", "best_model_RandomForest.joblib")
model = joblib.load(MODEL_PATH)

st.set_page_config(
    page_title="Prédiction Taxi NYC",
    page_icon="🚖",
    layout="centered"
)

st.markdown(
    """
    <div style='
        border: 3px solid #4CAF50; 
        border-radius: 10px; 
        padding: 12px; 
        text-align: center; 
        margin-bottom: 1em;
        background-color: #f9f9f9;
    '>
        <h1 style='margin: 0;'>🚖 Prédiction du montant total - Taxis NYC</h1>
    </div>
    <p style='text-align: center; font-size: 1.1em; margin-top: 0.5em;'>
        Cette application utilise un modèle <b>Random Forest</b> pour estimer le montant total
        d'une course de taxi à New York à partir de ses caractéristiques.
    </p>
    """,
    unsafe_allow_html=True
)


if not os.path.exists(MODEL_PATH):
    st.error(f"Le modèle n'a pas été trouvé à l'emplacement : `{MODEL_PATH}`")
    st.stop()

model = joblib.load(MODEL_PATH)

# ========================
# --- Formulaire utilisateur ---
# ========================
form_container = st.container()
with form_container:
    with st.form("prediction_form"):
        st.subheader("📋 Saisir les informations de la course")
        
        passenger_count = st.number_input("Nombre de passagers", min_value=1, max_value=10, value=1)
        trip_distance = st.number_input("Distance du trajet (miles)", min_value=0.0, value=1.0)
        fare_amount = st.number_input("Montant de base ($)", min_value=0.0, value=5.0)
        extra = st.number_input("Extra ($)", min_value=0.0, value=0.0)
        mta_tax = st.number_input("Taxe MTA ($)", min_value=0.0, value=0.5)
        tip_amount = st.number_input("Pourboire ($)", min_value=0.0, value=0.0)
        tolls_amount = st.number_input("Péages ($)", min_value=0.0, value=0.0)
        payment_type = st.selectbox("Type de paiement", ["Credit_Card", "Cash"])
        
        submitted = st.form_submit_button("🔍 Prédire")

# ========================
# --- Prédiction ---
# ========================
if submitted:
    # Création du DataFrame d'entrée
    input_df = pd.DataFrame([{
        "passenger_count": passenger_count,
        "trip_distance": trip_distance,
        "fare_amount": fare_amount,
        "extra": extra,
        "mta_tax": mta_tax,
        "tip_amount": tip_amount,
        "tolls_amount": tolls_amount,
        "payment_type": payment_type
    }])
    
    # --- Affichage des données saisies ---
    st.write("### 📄 Données saisies")
    st.dataframe(input_df)

    # --- Prétraitement du payment_type si nécessaire ---
    if "payment_type" in model.feature_names_in_:
        # Si le modèle attend la colonne "payment_type" en numérique ou one-hot
        input_df = pd.get_dummies(input_df, columns=["payment_type"])
        # Ajouter les colonnes manquantes que le modèle attend
        for col in model.feature_names_in_:
            if col not in input_df.columns:
                input_df[col] = 0
        input_df = input_df[model.feature_names_in_]

    # --- Prédiction sécurisée ---
    try:
        prediction = round(model.predict(input_df)[0], 2)
        st.success(f"💵 Montant total estimé : **{prediction} $**")
    except Exception as e:
        st.error(f"Erreur lors de la prédiction : {e}")