# main.py
import pandas as pd
from src.analyse_exploratoire import AnalyseEploratoireDonnees
from src.data_processing import PretraitementsDonnees
from src.modalite_chiffre import ModaliteeChiffre
from src.tests_statistiques import TestsStatistiques
from src.clustering import Clustering
from src.improvability_score import ImprovabilityScore
from src.dashboard import Dashboard

def main():
    
    path = "data/exercice_data.csv"
    exploration_donnees = AnalyseEploratoireDonnees(path)
    data = exploration_donnees.importer_donnees(path)
    
    data.drop(columns = ['FirstName', 'FamilyName'], inplace= True)
    numeric_columns = data.select_dtypes(include=['int64']).columns
    categorical_columns = data.select_dtypes(include=['object']).columns
    
    
    pretraitement = PretraitementsDonnees(data)
    
    #Encodage des variables catégorielles
    data_encoded = pretraitement.encodage_var_categorielles(categorical_columns)
    
    data_encoded_new = data_encoded.copy()
    data_encoded_new = data_encoded.drop(columns = ['Fedu', 'Mjob', 'Walc'])
    
    #Scaling des données 
    data_scaled = pretraitement.scale_data(data_encoded_new)
        
    #kmeans clustering
    Kmeans_clustering = Clustering(data_encoded_new, data_scaled)
    data_with_cluster = Kmeans_clustering.kmeans(6)
    
    #k_means_resultats
    resultat = Kmeans_clustering.analyse_kmeans(data_with_cluster)

    
    #Improvability_score
    improvability_score = ImprovabilityScore(resultat)
    data_finale = improvability_score.assign_support_level(data_encoded_new)
    
    dashboard = Dashboard(data_finale)
    dashboard.run()


if __name__ == "__main__":
    main()