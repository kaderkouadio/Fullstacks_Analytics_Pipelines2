# Fullstacks_Analytics_Pipelines2

# 🚖 Taxi Driver App – Analyse et Visualisation des Courses

Ce dépôt correspond à la Phase 2 du projet Fullstacks_Analytics_Pipelines.
Il s’appuie directement sur les données préparées et le modèle entraîné lors de la Phase 1 (pipeline ELT + modélisation) pour proposer une application web interactive développée avec Streamlit.
L’objectif est de permettre aux utilisateurs (scientifiques de données, analystes, décideurs) :
De visualiser les données traitées de manière interactive
D’explorer les tendances et insights à travers des graphiques dynamiques
De faire des prédictions en temps réel grâce au modèle de Machine Learning pré-entraîné

---

### 🎯 Objectifs du Dépôt 2

1. **Interface Utilisateur Interactive**
  -Développement d’une application web responsive avec Streamlit
  -Navigation multi-pages (Accueil, Visualisation, Prédiction, À propos)

2. **Visualisation Dynamique des Données**
  -Graphiques interactifs avec Plotly et Altair
  -Filtres et sélections en temps réel

3. **Prédiction en Direct**
  -Chargement du modèle ML exporté de la Phase 1
  -Saisie de paramètres par l’utilisateur via formulaires
  -Retour immédiat du résultat de la prédiction

4. **Expérience Utilisateur**
  -Ajout d’animations Lottie pour dynamiser l’interface
  -Mise en place d’un design cohérent et professionnel

### 🛠 Fonctionnalités Principales

1. **Exploration des données** :

  -Tableaux interactifs filtrables
  -Graphiques comparatifs
  -Analyse descriptive rapide

1. **Prédiction** :

  -Interface simple pour saisir les variables d’entrée
  -Résultats calculés instantanément par le modèle
  -Affichage des probabilités et de la classe prédite

3. **Pages dédiées** :

  -Accueil : présentation du projet et de son objectif
  -Analyse : exploration des données
  -Prédiction : simulation en direct
  -À propos : informations sur l’auteur et le projet

## 📦 Livrables

- Application **Streamlit multi-pages** prête à l’emploi
- Code Python structuré et documenté
- Fichiers de configuration pour le déploiement
- Documentation utilisateur (ce README)


## 🚀 Technologies Utilisées

- **Langage** : Python 3.x

- **Framework Web** : Streamlit

- **Visualisation** : Plotly, Altair, Matplotlib

- **Machine Learning** : scikit-learn, XGBoost, CatBoost (modèle pré-entraîné en Phase 1)

- **Animations** : streamlit-lottie

- **Gestion des dépendances** : pip + requirements.txt

- **Déploiement** : Streamlit 

## 📌 Fonctionnalités

- 📊 **Tableau de bord interactif** avec des graphiques sur les courses.
- 🗺 **Carte interactive** pour visualiser les trajets.
- 📅 Filtrage par date, heure ou jour de la semaine.
- 📍 Analyse par zones de départ et d’arrivée.
- 📈 Statistiques clés : distance moyenne, revenu total, temps de trajet moyen.
- 🎨 Interface moderne avec **Lottie animations**.

---

## 🛠️ Installation

### 1️⃣ Cloner le dépôt

git clone https://github.com/kaderkouadio/Fullstacks_Analytics_Pipelines2

cd App_streamlit

### 2 Créer un environnement virtuel 

python -m venv .venv
source .venv/bin/activate   # macOS/Linux
.\venv\Scripts\activate     # Windows

-----

### 3.Installer les dépendances

pip install -r requirements.txt

4. Lancer l’application

streamlit run dashboard.py

## 🔗 Me retrouver

[💼 LinkedIn](https://www.linkedin.com/in/koukou-kader-kouadio-2a32371a4/)

📧 [Email](mailto:kkaderkouadio@gmail.com)
