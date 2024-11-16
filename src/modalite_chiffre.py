""""
Cette classe permet de créer une correspondance entre les anciennes valeurs des variables catégorielles 
et leurs nouvelles valeurs numériques encodées. Elle est utile pour interpréter les variables catégorielles 
après encodage.
"""


class ModaliteeChiffre:
    def __init__(self, data):
        self.data = data

    def dict_modalité_chiffre(self, categorical_columns):
        df = self.data.copy()
        correpondance_category_chiffre = {}
        for col in categorical_columns:
            df[col] = df[col].astype("category")
            df[f"{col}_encoded"] = df[col].cat.codes
            correpondance_category_chiffre[col] = dict(
                enumerate(df[col].cat.categories)
            )
        return correpondance_category_chiffre
