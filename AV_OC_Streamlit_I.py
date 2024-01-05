# Importation des bibliothèques nécessaires
import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler

# Définir la fonction pour la détection des billets
def detecteur_billets(df, modele):
    # Sélection des colonnes
    colonnes_selectionnees = ["diagonal", "height_left", "height_right", "margin_low", "margin_up", "length"]
    df_numerique = df[colonnes_selectionnees]

    # Application du StandardScaler aux colonnes numériques
    scaler = StandardScaler()
    echantillons_scaled = scaler.fit_transform(df_numerique)

    # Utilisation du modèle pour les prédictions
    predictions = modele.predict(echantillons_scaled)

    # Ajout des prédictions en tant que nouvelle colonne
    df["Prédiction"] = predictions

    # Affichage des résultats
    st.subheader("Résultats de la détection de billets :")
    st.dataframe(df)  # Affiche le DataFrame avec les prédictions
    st.bar_chart(df["Prédiction"].value_counts())

# Chargement du modèle logistique pré-entraîné
modele_logistique = joblib.load('modele_logistique.pkl')

# Interface utilisateur Streamlit
st.title("Détecteur de faux billets")
st.markdown(
    "par Anthony VIDRAGO pour OC - 08/12/2023"
)
st.markdown(
    "Cette application utilise un modèle de détection pour classer les billets 'Anthentique' ou 'Contrefait' en fonction de leurs caractéristiques.")


# Chargement du fichier CSV
uploaded_file = st.file_uploader("Charger votre fichier CSV")

if uploaded_file is not None:
    # Charger le fichier CSV en DataFrame
    df = pd.read_csv(uploaded_file, sep=",")

    # Appeler la fonction detecter_billets pour effectuer la détection
    detecteur_billets(df, modele_logistique)
