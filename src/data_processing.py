from sklearn.preprocessing import StandardScaler

"""
Etape 2: Traitement des données
Cette classe permet de prétraiter les données et les restructurer en  encodant les variables catégorielles 
afin de les transformer en valeurs numériques compatibles avec les algorithmes de modélisation.
"""


class PretraitementsDonnees:
    def __init__(self, data):
        self.data = data

    # Cette méthode transforme chaque variable catégorielle en codes numériques, où chaque catégorie unique reçoit un entier unique.
    def encodage_var_categorielles(self, categorical_columns):
        df = self.data.copy()
        for col in categorical_columns:
            df[col] = df[col].astype("category")
            df[col] = df[col].cat.codes
        return df

    # Cette méthode permet de stardiser les données numériques pour les rendre utilisables lors de l'étape 3 du clustering
    def scale_data(self, df, numerical_columns):
        df_ = df.copy()
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(df_[numerical_columns])
        df_[numerical_columns] = X_scaled
        return df_
