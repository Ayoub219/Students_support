from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

class Clustering:
    
    def __init__(self, data_encoded_new, data_scaled):
        self.data_encoded_new = data_encoded_new
        self.data_scaled = data_scaled
        #self.n_clusters = n_clusters
        
    def regle_coude(self):
        inertias = []
        K_range = range(1, 11)  # Tester de 1 à 10 clusters

        for k in K_range:
            kmeans = KMeans(n_clusters=k, random_state=0)
            kmeans.fit(self.data_scaled)
            inertias.append(kmeans.inertia_)
        # Tracer le graphe de la règle du coude
        plt.figure(figsize=(8, 5))
        plt.plot(K_range, inertias, marker='o')
        plt.xlabel('Nombre de clusters k')
        plt.ylabel("Inertie (somme des distances au carré)")
        plt.title("Méthode du coude pour déterminer le nombre optimal de clusters")
        plt.show()
        
    def kmeans(self, n_clusters):
        """Applique KMeans pour effectuer le clustering."""
        kmeans = KMeans(n_clusters)  # Ajuste le nombre de clusters selon tes besoins
        self.data_encoded_new['cluster'] = kmeans.fit_predict(self.data_scaled)
        return self.data_encoded_new
    
    def analyse_kmeans(self, data_with_cluster):
        data_kmeans_analisis = data_with_cluster.groupby("cluster").mean() 
        return data_kmeans_analisis.sort_values(by = 'FinalGrade', ascending = False)
