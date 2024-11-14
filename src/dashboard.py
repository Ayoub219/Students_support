import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from src.clustering import Clustering


class Dashboard:
    def __init__(self, data):
        self.data = data
        st.title("Dashboard d'Analyse de Données")
        st.write("Explorez les différentes visualisations pour analyser les performances et le potentiel d'amélioration des élèves.")
        self.create_sidebar_filters() 
    
    def create_sidebar_filters(self):
        # Filter based on 'sex'
        sex_options = self.data['sex'].unique()
        selected_sex = st.sidebar.multiselect("Sexe", options=sex_options, default=sex_options)

        # Filter based on 'age'
        age_min, age_max = int(self.data['age'].min()), int(self.data['age'].max())
        selected_age = st.sidebar.slider("Âge", min_value=age_min, max_value=age_max, value=(age_min, age_max))

        # Apply filters
        self.data = self.data[(self.data['sex'].isin(selected_sex)) &
                              (self.data['age'].between(*selected_age))]

    def visualisation1(self):
        st.subheader("Priorisation des Élèves à Accompagner")
        x = self.data['FinalGrade']
        y = self.data['Improvability_score']
        random_offset = np.random.normal(0, 0.2, size=y.shape) 
        plt.figure(figsize=(10, 6))
        plt.scatter(x, y + random_offset, s=7)
        plt.gca().invert_xaxis()
        plt.xlabel("FinalGrade")
        plt.ylabel("Improvability_score")
        plt.title("Priorisation des Élèves à Accompagner")
        st.pyplot(plt)

    def visualisation2(self):
        st.subheader("Distribution des Notes Actuelles")
        plt.figure(figsize=(10, 6))
        plt.hist(self.data['FinalGrade'], bins=20, color='blue', alpha=0.7)
        plt.xlabel("Final Grade")
        plt.ylabel("Nombre d'Élèves")
        plt.title("Distribution des Notes Actuelles")
        st.pyplot(plt)
        
    def visualisation3(self):
        st.subheader("Distribution de l'Improvability Score")
        plt.figure(figsize=(10, 6))
        plt.hist(self.data['Improvability_score'], bins=20, color='green', alpha=0.7)
        plt.xlabel("Improvability_score")
        plt.ylabel("Nombre d'Élèves")
        plt.title("Distribution de Improvability_score")
        st.pyplot(plt)
        
    def visualisation4(self):
        st.subheader("Boxplot: Improvability Score en Fonction de la Note")
        plt.figure(figsize=(10, 6))
        sns.boxplot(x=self.data['Improvability_score'], y=self.data['FinalGrade'], palette="Blues")
        plt.xlabel("Complexité de l'Accompagnement")
        plt.ylabel("Note Actuelle")
        plt.title("Boxplot: Improvability Score en Fonction de la Note")
        st.pyplot(plt)
        
    def visualisation5(self):
        st.subheader("Moyenne des Notes en Fonction de l'Improvability Score")
        avg_grades_by_complexity = self.data.groupby('Improvability_score')['FinalGrade'].mean()
        plt.figure(figsize=(10, 6))
        avg_grades_by_complexity.plot(kind='bar', color='skyblue')
        plt.xlabel("Complexité de l'Accompagnement")
        plt.ylabel("Note Moyenne")
        plt.title("Moyenne des Notes en Fonction de l'Improvability Score")
        st.pyplot(plt)

    def run(self):
        self.visualisation1()
        # Organisation des visualisations dans un dashboard structuré
        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                self.visualisation2()
            with col2:
                self.visualisation3()
        
        st.markdown("---")  # Ligne de séparation entre les sections
        
        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                self.visualisation4()
            with col2:
                self.visualisation5()

        
