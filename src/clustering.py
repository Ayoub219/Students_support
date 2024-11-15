from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
from kmodes.kprototypes import KPrototypes

class Clustering:
    
    def __init__(self, data_encoded, data_scaled):
        self.data_encoded = data_encoded
        self.data_scaled = data_scaled
        
    def regle_coude(self):
        numeric_columns = ['age', 'absences', 'FinalGrade']
        self.data_scaled[numeric_columns] = self.data_scaled[numeric_columns].astype(float)
        categorical_columns_index = [self.data_scaled.columns.get_loc(col) for col in self.data_scaled.columns if col not in numeric_columns]
        
        inertias = []
        K_range = range(1, 11)  

        for k in K_range:
            kprot = KPrototypes(n_clusters=k, init='Huang', random_state=42)
            kprot.fit_predict(self.data_scaled.values, categorical = categorical_columns_index)
            inertias.append(kprot.cost_)
            
        sns.set_theme(style="whitegrid", palette="bright", font_scale=1.2)
        
        plt.figure(figsize=(15, 7))
        ax = sns.lineplot(x=K_range, y=inertias, marker="o", dashes=False)
        ax.set_title('Elbow curve', fontsize=18)
        ax.set_xlabel('No of clusters', fontsize=14)
        ax.set_ylabel('Cost', fontsize=14)
        plt.show()
        
    def Kprototypes(self, n_clusters):
        numeric_columns = ['age', 'absences', 'FinalGrade']
        self.data_scaled[numeric_columns] = self.data_scaled[numeric_columns].astype(float)
        categorical_columns_index = [self.data_scaled.columns.get_loc(col) for col in self.data_scaled.columns if col not in numeric_columns]
        
        kprot = KPrototypes(n_clusters, init = 'Huang', random_state = 42) 
        self.data_encoded['cluster'] = kprot.fit_predict(self.data_scaled.values, categorical = categorical_columns_index)
        return self.data_encoded
    
    def analyse_Kprototypes(self, data_with_cluster):
        data_kprorotypes_analisis = data_with_cluster.groupby("cluster").mean() 
        return data_kprorotypes_analisis.sort_values(by = 'FinalGrade', ascending = False)
