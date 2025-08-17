import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
from utils import load_parquet_data


# --- Configuration des chemins ---
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "output"

# Fonction utilitaire pour charger un parquet

# --- Titre principal ---
st.title("🚖 Analyse Exploratoire des Courses de Taxi")
st.markdown("Visualisation interactive des données transformées : tendances mensuelles, distribution des passagers et analyse par type de paiement.")

# --- Chargement des datasets ---
monthly_df = load_parquet_data("monthly_summary.parquet")
passengers_df = load_parquet_data("passenger_count_distribution.parquet")
payments_df = load_parquet_data("payment_type_summary.parquet")

# =======================
# 1️⃣ Tendances mensuelles
# =======================
st.subheader("📅 Évolution mensuelle")
selected_metrics = st.multiselect(
    "Choisissez les indicateurs à afficher :",
    options=["trips_count", "total_amount_sum", "avg_trip_distance", "avg_fare_amount", "avg_tip_amount"],
    default=["trips_count", "total_amount_sum"]
)

fig_monthly = px.line(
    monthly_df,
    x="year_month",
    y=selected_metrics,
    markers=True,
    title="📆 Trajets et Montants par Mois"
)
st.plotly_chart(fig_monthly, use_container_width=True)

st.divider()

# =======================
# 2️⃣ Distribution des passagers & Paiement
# =======================
col1, col2 = st.columns(2)

with col1:
    st.subheader("🧍 Nombre de passagers")
    fig_passengers = px.bar(
        passengers_df,
        x="passenger_count", y="count",
        title="Distribution du nombre de passagers",
        labels={"passenger_count": "Passagers", "count": "Nombre de trajets"},
        color="count",
        color_continuous_scale="viridis"
    )
    st.plotly_chart(fig_passengers, use_container_width=True)

with col2:
    st.subheader("💳 Type de paiement")
    fig_payments = px.bar(
        payments_df,
        x="payment_type", y="avg_amount",
        title="Montant moyen par type de paiement",
        labels={"payment_type": "Type de paiement", "avg_amount": "Montant moyen ($)"},
        color="avg_amount",
        color_continuous_scale="plasma"
    )
    st.plotly_chart(fig_payments, use_container_width=True)

st.divider()

# =======================
# 3️⃣ Filtre interactif mensuel
# =======================
st.subheader("🎯 Focus sur un mois particulier")
selected_month = st.selectbox(
    "Sélectionnez un mois :",
    options=monthly_df["year_month"].unique()
)

focus_data = monthly_df[monthly_df["year_month"] == selected_month]
st.write(f"**Statistiques du {selected_month} :**")
st.dataframe(focus_data)
