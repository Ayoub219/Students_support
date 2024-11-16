"""
Étape 4: Détermination d'un score pour l'accompagnement des élèves
Cette classe détermine un niveau de suivi ou de soutien pour les élèves en fonction du cluster 
auquel ils appartiennent. Chaque cluster est associé à un score d'accompagnement, qui peut être 
utilisé pour adapter les interventions pédagogiques.
"""


class ImprovabilityScore:
    def __init__(self, table):
        self.table = table

    def improvability_score(self, data):
        # Création d'un dictionnaire où chaque cluster est mappé à un score
        cluster_score = {
            cluster: score for score, cluster in enumerate(self.table.index, start=1)
        }
        # Associer les scores aux observations en fonction du cluster
        data["Improvability_score"] = data["cluster"].map(cluster_score)
        return data
