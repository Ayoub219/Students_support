# main.py
from src.analyse_exploratoire import AnalyseEploratoireDonnees
from src.data_processing import PretraitementsDonnees
from src.modalite_chiffre import ModaliteeChiffre
from src.clustering import Clustering
from src.improvability_score import ImprovabilityScore
from src.dashboard import Dashboard


def main():

    path = "data/exercice_data.csv"
    exploration_donnees = AnalyseEploratoireDonnees(path)

    # Importer donnees
    data = exploration_donnees.importer_donnees(path)
    data.drop(columns=["FirstName", "FamilyName"], inplace=True)

    # Pretraitement données
    pretraitement = PretraitementsDonnees(data)
    # Encodage des variables catégorielles
    categ_col = data.select_dtypes(include=["object"]).columns
    data_encoded = pretraitement.encodage_var_categorielles(categ_col)
    # Scaling des données
    num_columns = ["age", "absences", "FinalGrade"]
    data_scaled = pretraitement.scale_data(data_encoded, num_columns)

    # kprototypes clustering
    Kprototypes_clustering = Clustering(data_encoded, data_scaled)
    # Appliquer la regle du coude pour determiner le nombre optimal de cluster
    #Kprototypes_clustering.regle_coude()
    # Demander à l'utilisateur d'entrer le nombre de clusters après l'analyse de la règle du coude
    # n_clusters = int(input("Entrez le nombre de clusters à utiliser : "))
    n_clusters = 4
    data_with_cluster = Kprototypes_clustering.Kprototypes(n_clusters)
    # k_prorotypes_resultats
    resultat = Kprototypes_clustering.analyse_Kprototypes(data_with_cluster)

    # Improvability_score
    improvability_score = ImprovabilityScore(resultat)
    data_finale = improvability_score.improvability_score(data_encoded)

    # Correspondace entre le nom de catégorie et son numéro
    corresp = ModaliteeChiffre(data)
    correpondance_category_chiffre = corresp.dict_modalité_chiffre(categ_col)
    print(correpondance_category_chiffre)

    # Dashboard
    dashboard = Dashboard(data_finale)
    dashboard.run()


if __name__ == "__main__":
    main()
