# main.py
import pandas as pd
from src.analyse_exploratoire import AnalyseEploratoireDonnees
from src.data_processing import PretraitementsDonnees
from src.modalite_chiffre import ModaliteeChiffre
from src.tests_statistiques import TestsStatistiques

def main():
    
    data = pd.read_csv("data/exercice_data.csv", delimiter=",", index_col = 0, encoding="ISO-8859-1")
    data.drop(columns = ['FirstName', 'FamilyName'], inplace= True)
    numeric_columns = data.select_dtypes(include=['int64']).columns
    categorical_columns = data.select_dtypes(include=['object']).columns
    
    
    analyse_exploratoire = AnalyseEploratoireDonnees(data)
    
    
    pretraitement = PretraitementsDonnees(data)
    
    
    #Encodage des variables catégorielles
    data_encoded = pretraitement.encodage_var_categorielles(categorical_columns)
    print(data_encoded.head())
    
    test = TestsStatistiques(data_encoded)
    anova = test.test_anova(categorical_columns)
    print(anova)
    
    #Scaling des données 
    #data_scaled = pretraitement.scale_data(data_encoded)
    #print(data_scaled)
        
    #Dictionnaire pour attribuer chaque modalité de la variable à son chiffre correspondant    
    #correspondance_modalite_chiffre = ModaliteeChiffre(data)
    #print(correspondance_modalite_chiffre.dict_modalité_chiffre(categorical_columns))
    
    
if __name__ == "__main__":
    main()