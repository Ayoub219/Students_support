import matplotlib.pyplot as plt
import seaborn as sns
from kmodes.kprototypes import KPrototypes

"""
Étape 3: Clustering et Segmentation des élèves
Cette classe permet de réaliser un clustering des élèves en fonctions des réponses qu'ils 
ont fournies afin de les segmenter en groupes homogènes en utilisant l'algorithme 
d'apprentissange non supervisé K-prototypes, util lorsque le dataset fournit à la fois 
des données numériques et catégorielles (données mixtes).
"""


class Clustering:

    def __init__(self, data_encoded, data_scaled):
        self.data_encoded = data_encoded
        self.data_scaled = data_scaled

    # Cette méthode applique la méthode de la "règle du coude" pour déterminer
    # le nombre optimal de clusters
    def regle_coude(self):
        numeric_columns = ["age", "absences", "FinalGrade"]
        self.data_scaled[numeric_columns] = self.data_scaled[numeric_columns].astype(
            float
        )

        # Liste des indices des colonnes catégorielles dans le DataFrame
        # (qui ne sont pas dans 'numeric_columns')
        categorical_columns_index = [
            self.data_scaled.columns.get_loc(col)
            for col in self.data_scaled.columns
            if col not in numeric_columns
        ]

        # Initialisation de la liste pour stocker les couts pour chaque valeur de k
        inertias = []
        K_range = range(1, 11)

        # Création du modèle K-Prototypes avec pour chaque valeur de k
        for k in K_range:
            kprot = KPrototypes(n_clusters=k, init="Huang", random_state=42)
            kprot.fit_predict(
                self.data_scaled.values, categorical=categorical_columns_index
            )
            inertias.append(kprot.cost_)

        # Création de la figure et tracé de la courbe du coude
        sns.set_theme(style="whitegrid", palette="bright", font_scale=1.2)

        plt.figure(figsize=(15, 7))
        ax = sns.lineplot(x=K_range, y=inertias, marker="o", dashes=False)
        ax.set_title("Elbow curve", fontsize=18)
        ax.set_xlabel("No of clusters", fontsize=14)
        ax.set_ylabel("Cost", fontsize=14)
        plt.show()

    # Applique le clustering K-Prototypes avec un nombre de clusters spécifié
    def Kprototypes(self, n_clusters):
        numeric_columns = ["age", "absences", "FinalGrade"]
        self.data_scaled[numeric_columns] = self.data_scaled[numeric_columns].astype(
            float
        )
        categorical_columns_index = [
            self.data_scaled.columns.get_loc(col)
            for col in self.data_scaled.columns
            if col not in numeric_columns
        ]

        # Création du modèle K-Prototypes avec le nombre de clusters spécifié
        kprot = KPrototypes(n_clusters, init="Huang", random_state=42)
        self.data_encoded["cluster"] = kprot.fit_predict(
            self.data_scaled.values, categorical=categorical_columns_index
        )
        return self.data_encoded

    # Cette méthode réalise une analyse de chaque cluster en calculant la moyenne
    # des variables pour chaque cluster.
    def analyse_Kprototypes(self, data_with_cluster):
        data_kprorotypes_analyse = data_with_cluster.groupby("cluster").mean()
        return data_kprorotypes_analyse.sort_values(by="FinalGrade", ascending=False)
