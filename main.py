# main.py
import pandas as pd
from src.analyse_exploratoire import AnalyseEploratoireDonnees
from src.data_processing import PretraitementsDonnees
from src.modalite_chiffre import ModaliteeChiffre
from src.tests_statistiques import TestsStatistiques
from src.clustering_kmeans import Clustering

def main():
    
    data = pd.read_csv("data/exercice_data.csv", delimiter=",", index_col = 0, encoding="ISO-8859-1")
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
    print(data_scaled)
        
    #kmeans clustering
    Kmeans_clustering = Clustering(data_encoded_new, data_scaled)
    data_with_cluster = Kmeans_clustering.kmeans(6)
    print(data_with_cluster.head())
    
    data_kmeans_analisis = data_with_cluster.groupby("cluster").mean() 
    print(data_kmeans_analisis)
    
    
if __name__ == "__main__":
    main()