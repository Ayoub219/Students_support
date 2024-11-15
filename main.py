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
    
    
    #Scaling des données 
    data_scaled = pretraitement.scale_data(data_encoded)
        
    #kprototypes clustering
    Kprototypes_clustering = Clustering(data_encoded, data_scaled)
    #Kprototypes_clustering.regle_coude()
    
    data_with_cluster = Kprototypes_clustering.Kprototypes(6)
    
    #k_means_resultats
    resultat = Kprototypes_clustering.analyse_Kprototypes(data_with_cluster)
    print(resultat)

    
    #Improvability_score
    improvability_score = ImprovabilityScore(resultat)
    data_finale = improvability_score.improvability_score(data_encoded)

    
    corresp = ModaliteeChiffre(data)
    correpondance_category_chiffre = corresp.dict_modalité_chiffre(categorical_columns)
    print(correpondance_category_chiffre)
    
    #Dahboard
    dashboard = Dashboard(data_finale)
    dashboard.run()


if __name__ == "__main__":
    main()