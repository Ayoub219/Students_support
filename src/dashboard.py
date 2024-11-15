import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class Dashboard:
    def __init__(self, data):
        self.data = data
        st.set_page_config(page_title="Dashboard Élèves", layout="wide")  # Configuration du layout
        st.title("Dashboard Pour l'analyse de la situation des élèves")
        self.create_sidebar_filters() 
    
    def create_sidebar_filters(self):
        st.sidebar.header("Filtres")
        
        # Filtre selon le sexe
        sex_options = self.data['sex'].unique()
        selected_sex = st.sidebar.multiselect("Sélectionner le Sexe", options=sex_options, default=sex_options)
        
        # Filtre selon l'adresse
        address_options = self.data['address'].unique()
        selected_address = st.sidebar.multiselect("Sélectionner l'Adresse", options=address_options, default=address_options)

        # Filtre consommation d'alcool
        dalc_options = self.data['Dalc'].unique()
        selected_dalc = st.sidebar.multiselect("Consommation Alcool", options=dalc_options, default=dalc_options)
        
        # Filtre selon l'âge
        age_min, age_max = int(self.data['age'].min()), int(self.data['age'].max())
        selected_age = st.sidebar.slider("Sélectionner l'Âge", min_value=age_min, max_value=age_max, value=(age_min, age_max))

        # Application des filtres
        self.data = self.data[(self.data['sex'].isin(selected_sex)) & 
                              (self.data['address'].isin(selected_address)) & 
                              (self.data['Dalc'].isin(selected_dalc)) & 
                              (self.data['age'].between(*selected_age))]

    def complexité_accompagnement_note(self):
        st.subheader("Priorisation des Élèves à Accompagner")
        x = self.data['FinalGrade']
        y = self.data['Improvability_score']
        random_offset = np.random.normal(0, 0.2, size=y.shape) 
        plt.figure(figsize=(10, 6))
        plt.scatter(x, y + random_offset, s=7, color='purple', alpha=0.6)
        plt.gca().invert_xaxis()
        plt.xlabel("Note Finale", fontsize=12, weight='bold')
        plt.ylabel("Improvability Score", fontsize=12, weight='bold')
        plt.title("Priorisation des Élèves", fontsize=14, weight='bold')
        st.pyplot(plt)

    def distribution_notes(self):
        st.subheader("Distribution des Notes Actuelles")
        plt.figure(figsize=(10, 6))
        plt.hist(self.data['FinalGrade'], bins=20, color='skyblue', alpha=0.7)
        plt.xlabel("Note Finale", fontsize=12, weight='bold')
        plt.ylabel("Nombre d'Élèves", fontsize=12, weight='bold')
        plt.title("Distribution des Notes", fontsize=14, weight='bold')
        st.pyplot(plt)
        
    def distibution_improvability_score(self):
        st.subheader("Distribution de l'Improvability Score")
        plt.figure(figsize=(10, 6))
        plt.hist(self.data['Improvability_score'], bins=20, color='green', alpha=0.7)
        plt.xlabel("Improvability Score", fontsize=12, weight='bold')
        plt.ylabel("Nombre d'Élèves", fontsize=12, weight='bold')
        plt.title("Distribution du Score d'Amélioration", fontsize=14, weight='bold')
        st.pyplot(plt)
        
    def barchart_moyenne_note_improvability_score(self):
        st.subheader("Moyenne des Notes par Improvability Score")
        avg_grades_by_complexity = self.data.groupby('Improvability_score')['FinalGrade'].mean()
        plt.figure(figsize=(10, 6))
        avg_grades_by_complexity.plot(kind='bar', color='lightcoral', edgecolor='black')
        plt.xlabel("Complexité de l'Accompagnement", fontsize=12, weight='bold')
        plt.ylabel("Note Moyenne", fontsize=12, weight='bold')
        plt.title("Moyenne des Notes par Improvability Score", fontsize=14, weight='bold')
        st.pyplot(plt)
        
    def show_improvability_score_distribution_by_categories(self, var):
        st.subheader(f"Fréquence des Modalités de {var} par Improvability Score")

        # Utilisation de pivot_table pour compter les occurrences de chaque modalité
        improvability_freq_table = self.data.pivot_table(index='Improvability_score', columns=var, aggfunc='size', fill_value=0)

        # Affichage du tableau dans Streamlit
        st.dataframe(improvability_freq_table)
        
    def run(self):
        # Priorisation et distribution des notes
        self.complexité_accompagnement_note()
        
        # Disposition des graphiques dans un layout structuré
        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                self.barchart_moyenne_note_improvability_score()
            with col2:
                self.distibution_improvability_score()
        
        st.markdown("---")  # Ligne de séparation entre les sections

        self.distribution_notes()
        
        st.markdown("---")
        
        # Sélection de la variable catégorielle
        category_options = ['Pstatus', 'Medu', 'Fjob', 'traveltime', 'schoolsup', 'higher', 'Fjob', 'health']
        selected_category = st.sidebar.selectbox("Sélectionner une variable pour la visualisation par Improvability Score", options=category_options)

        # Visualisation des fréquences par Improvability Score
        self.show_improvability_score_distribution_by_categories(selected_category)

