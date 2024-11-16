import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

""""
Étape 5: Création d'un dashboard avec des visuels représentatifs en utilisant Streamlit
"""


class Dashboard:
    # Initialisation du Dashboard en configurant la page Streamlit et en définissant les filtres
    # de la barre latérale
    def __init__(self, data):
        self.data = data
        st.set_page_config(page_title="Dashboard Élèves", layout="wide")
        st.title("Dashboard Pour l'analyse de la situation des élèves")
        self.creation_filtres()

    # Cette méthode permet de créer les filtres pour permettre à l'utilisateur de sélectionner des
    # sous-ensembles de données
    def creation_filtres(self):
        st.sidebar.header("Filtres")

        # Filtre selon le sexe
        sexe_categories = self.data["sex"].unique()
        sexe_filtre = st.sidebar.multiselect(
            "Sélectionner le Sexe", options=sexe_categories, default=sexe_categories
        )

        # Filtre selon l'adresse
        address_categories = self.data["address"].unique()
        address_filtre = st.sidebar.multiselect(
            "Sélectionner l'Adresse",
            options=address_categories,
            default=address_categories,
        )

        # Filtre consommation d'alcool
        dalc_categories = self.data["Dalc"].unique()
        dalc_filtre = st.sidebar.multiselect(
            "Consommation Alcool", options=dalc_categories, default=dalc_categories
        )

        # Filtre selon l'âge
        age_min, age_max = int(self.data["age"].min()), int(self.data["age"].max())
        age_filtre = st.sidebar.slider(
            "Sélectionner l'Âge",
            min_value=age_min,
            max_value=age_max,
            value=(age_min, age_max),
        )

        # Application des filtres
        self.data = self.data[
            (self.data["sex"].isin(sexe_filtre))
            & (self.data["address"].isin(address_filtre))
            & (self.data["Dalc"].isin(dalc_filtre))
            & (self.data["age"].between(*age_filtre))
        ]

    # Cette méthode permet de dessiner le nuage de points montrant la dispersion des élèves
    # en fonction de leur note finale et de leur score d'accompagnement (Improvability Score)
    def score_accompagnement_note(self):
        st.subheader("Priorisation des Élèves à Accompagner")
        x = self.data["FinalGrade"]
        y = self.data["Improvability_score"]
        random_offset = np.random.normal(0, 0.2, size=y.shape)
        plt.figure(figsize=(8, 4))
        plt.scatter(x, y + random_offset, s=7, color="purple", alpha=0.6)
        plt.gca().invert_xaxis()
        plt.xlabel("Note Finale", fontsize=12, weight="bold")
        plt.ylabel("Improvability Score", fontsize=12, weight="bold")
        plt.title("Priorisation des élèves", fontsize=14, weight="bold")
        st.pyplot(plt)

    # Cette méthode trace l'histogramme de la distribution des scores d'accompagnement des élèves
    def distibution_improvability_score(self):
        st.subheader("Distribution de Improvability Score")
        plt.figure(figsize=(10, 6))
        plt.hist(self.data["Improvability_score"], bins=20, color="green", alpha=0.7)
        plt.xlabel("Improvability score", fontsize=12, weight="bold")
        plt.ylabel("Nombre d'Élèves", fontsize=12, weight="bold")
        plt.title("Distribution du score d'accompagnement", fontsize=14, weight="bold")
        st.pyplot(plt)

    # Cette méthode trace un graphique en barres montrant la moyenne des notes finales par niveau
    # de score d'accompagnement
    def barchart_moyenne_note_improvability_score(self):
        st.subheader("Moyenne des Notes par Improvability Score")
        avg_grades_by_complexity = self.data.groupby("Improvability_score")[
            "FinalGrade"
        ].mean()
        plt.figure(figsize=(10, 6))
        avg_grades_by_complexity.plot(kind="bar", color="lightcoral", edgecolor="black")
        plt.xlabel("Improvability score", fontsize=12, weight="bold")
        plt.ylabel("Note Moyenne", fontsize=12, weight="bold")
        plt.title(
            "Moyenne des notes par score d'accompagnement", fontsize=14, weight="bold"
        )
        st.pyplot(plt)

    # Cette méthode renvoie un tableau des pourcentages que présente les variables pour chaque
    # score d'accompagnement
    def pourcentage_modalite_improvability_score(self, var):
        st.subheader(f"Pourcentage des modalités de {var} par score d'accompagnement")

        improvability_freq_percentage = (
            pd.crosstab(
                index=self.data["Improvability_score"],
                columns=self.data[var],
                normalize="index",
            )
            * 100
        )
        st.dataframe(improvability_freq_percentage)

    # Cette méthode permet d'affichage les analyses de données, les visualisations et les filtres
    # dans une interface Streamlit
    def run(self):
        self.score_accompagnement_note()

        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                self.barchart_moyenne_note_improvability_score()
            with col2:
                self.distibution_improvability_score()

        st.markdown("---")

        category_options = [
            "Dalc",
            "Pstatus",
            "Medu",
            "Fjob",
            "traveltime",
            "schoolsup",
            "higher",
            "Fjob",
            "health",
        ]
        selected_category = st.sidebar.selectbox(
            "Sélectionner une variable pour la visualisation par Improvability Score",
            options=category_options,
        )
        self.pourcentage_modalite_improvability_score(selected_category)
