import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

class AnalyseEploratoireDonnees:
    def __init__(self, path):
        self.data = None
        if path:
            self.importer_donnees(path)
            
    def importer_donnees(self, path):
        self.data = pd.read_csv(path, delimiter=",", index_col = 0, encoding="ISO-8859-1")
        return self.data
    
        
    def afficher_premieres_lignes(self):
        return self.data.head()
    
    def taille_dataset(self):
        return self.data.shape
    
    def type_variables(self):
        return self.data.dtypes()
    
    def pourcentage_val_manquantes(self):
        return ((self.data.isna().sum()/self.data.shape[0]).sort_values(ascending=False))*100
    
    def statistiques_descriptives(self):
        return self.data.describe()
    
    def distribution_variable_numerique(self, variable):
        sns.histplot(self.data[variable], bins=20,kde= True, color='skyblue', edgecolor='black')
        plt.xlabel('Valeurs')
        plt.ylabel('Fréquence')
        plt.title(f"Distribution de {variable}")
        plt.show()
        
    def matrice_correlation(self):
        plt.figure(figsize=(8, 6)) 
        sns.heatmap(self.data.corr(), annot=True, cmap='coolwarm', fmt=".2f")
        plt.show()

    def modalites_var_categorielles(self, categorical_columns):
        value_counts = {}
        for column in categorical_columns:
            value_counts[column] = self.data[column].value_counts()
        return value_counts
