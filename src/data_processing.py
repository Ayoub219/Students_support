from sklearn.preprocessing import StandardScaler


class PretraitementsDonnees:
    def __init__(self, data):
        self.data = data
        
    def encodage_var_categorielles(self, categorical_columns):
        df = self.data.copy()
        for col in categorical_columns:
            df[col] = df[col].astype('category')
            df[col] = df[col].cat.codes
        return df
    
    def scale_data(self, df):
        df_ = df.copy()
        scaler = StandardScaler()
        columns = df_.columns
        X = df_[columns]
        X_scaled = scaler.fit_transform(X)
        return X_scaled
    