import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

class AnalyseEploratoireDonnees:
    def __init__(self, data):
        self.data = data
        
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
    
    def matrice_correlation(self, numeric_columns):
        plt.figure(figsize=(8, 6)) 
        df_numerical_variables = self.data[numeric_columns]
        sns.heatmap(df_numerical_variables.corr(), annot=True, cmap='coolwarm', fmt=".2f")
        plt.show()

    def modalites_var_categorielles(self, categorical_columns):
        value_counts = {}
        for column in categorical_columns:
            value_counts[column] = self.data[column].value_counts()
        return value_counts
