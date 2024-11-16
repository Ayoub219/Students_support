import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

"""
Etape 1: Analyse exploratoire des données
Cette classe permet de réaliser une analyse exploratoire des données pour
mieux comprendre la composition du dataset ainsi que le type de variables
et leurs distributions.
"""


class AnalyseEploratoireDonnees:
    def __init__(self, path):
        self.data = None
        # Si le chemin du fichier est bien fourni, on importe les données à partir du fichier
        if path:
            self.importer_donnees(path)

    # Cette méthode permet d'importer les données
    def importer_donnees(self, path):
        self.data = pd.read_csv(path, delimiter=",", index_col=0, encoding="ISO-8859-1")
        return self.data

    # Cette méthode permet d'afficher les premières lignes de notre dataset
    def afficher_premieres_lignes(self):
        return self.data.head()

    # Cette méthode permet d'afficher le nombre de lignes et de colonnes
    def taille_dataset(self):
        return self.data.shape

    # Cette méthode renvoie le types des variables
    def type_variables(self):
        return self.data.dtypes()

    # Cette méthode renvoie le pourcentage de valeurs manquantes au niveau de
    # chaque variable(colonne)
    def pourcentage_val_manquantes(self):
        pourcentage_nan = (self.data.isna().sum() / self.data.shape[0]) * 100
        pourcentage_nan = pourcentage_nan.sort_values(ascending=False)
        return pourcentage_nan

    # Cette méthode permet de renvoyer des statistiques des variables
    # numériques (mean - median - min- max ...)
    def statistiques_descriptives(self):
        return self.data.describe()

    # Cette méthode permet de tracer l'histogramme et la ditribution des
    # variables numériques
    def distribution_variable_numerique(self, variable):
        sns.histplot(
            self.data[variable], bins=20, kde=True, color="skyblue", edgecolor="black"
        )
        plt.xlabel("Valeurs")
        plt.ylabel("Fréquence")
        plt.title(f"Distribution de {variable}")
        plt.show()

    # Cette méthode permet de tracer un heatmap pour visualiser les
    # corrélations entre les variables
    def matrice_correlation(self):
        plt.figure(figsize=(8, 6))
        sns.heatmap(self.data.corr(), annot=True, cmap="coolwarm", fmt=".2f")
        plt.show()

    # Cette méthode renvoie les modalités qui constituent les variables
    # catégorielle
    def modalites_var_categorielles(self, categorical_columns):
        value_counts = {}
        for column in categorical_columns:
            value_counts[column] = self.data[column].value_counts()
        return value_counts
