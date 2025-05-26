# 💶 Détecteur de faux billets – Application Streamlit

Ce dépôt contient une **application web Streamlit** conçue dans le cadre du Projet 10 (*Détectez des faux billets avec Python*) du parcours *Data Analyst* chez OpenClassrooms. L’application permet de charger un fichier CSV contenant des caractéristiques physiques de billets en euros, puis de détecter automatiquement les faux billets à l’aide d’un modèle de classification.

---

## 🧠 Objectif

> Proposer un outil interactif capable de prédire si un billet est authentique ou contrefait, à partir de ses dimensions.

---

## 🛠️ Fonctionnalités

- Chargement d’un fichier CSV avec les variables suivantes :
  - `diagonal`, `height_left`, `height_right`, `margin_low`, `margin_up`, `length`
- Prétraitement automatique avec **StandardScaler**
- Prédiction par un **modèle de régression logistique** pré-entraîné (`modele_logistique.pkl`)
- Affichage :
  - d’un tableau des prédictions
  - d’un histogramme (bar chart) du nombre de billets vrais/faux

---

## 🧪 Modèle utilisé

- Modèle : **Régression logistique**
- Prétraitement : **StandardScaler**
- Format : fichier pickle `modele_logistique.pkl`

---

## 🚀 Lancer l’application en local

### 1. Cloner le dépôt

```bash
git clone https://github.com/ton_compte/app_streamlit_billets.git
cd app_streamlit_billets
```

### 2. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 3. Démarrer l’application

```bash
streamlit run app.py
```

---

## 📁 Structure du projet

```
├── app.py                     → Code principal de l’application Streamlit
├── modele_logistique.pkl      → Modèle entraîné (pickle)
├── exemple.csv                → Fichier exemple à charger
├── requirements.txt           → Dépendances Python
└── README.md                  → Présentation du projet
```

---

## 📊 Exemple de sortie

- Résultat sous forme de DataFrame avec la colonne **"Prédiction"**
- Diagramme à barres affichant le nombre de billets **authentiques** vs **contrefaits**

---

## 📄 Licence

Projet réalisé à but éducatif dans le cadre d’une formation chez OpenClassrooms.  
Les données utilisées sont simulées et ne représentent pas des billets réels.

---

## 👨‍💻 Auteur

Application développée par **AnthonyJVID** – Projet 10 – OpenClassrooms  
Date : 08/12/2023
