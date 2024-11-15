import unittest
import pandas as pd
from src.clustering import Clustering  

class TestClustering(unittest.TestCase):

    def setUp(self):
        # Simuler des données pour le test
        data_encoded = {
            'sex': [1, 1, 0, 1, 0],
            'age': [15, 17, 16, 18, 20],
            'address': [0, 0, 1, 1, 0],
            'absences': [10, 20 , 35 , 2, 10],
            'FinalGrade': [30, 23, 2, 90, 10]
        }
        
        data_scaled = {
            'sex': ['F', 'M', 'F', 'M', 'F'],
            'age': [15, 17, 16, 18, 20],
            'address': ['R', 'R', 'U', 'R', 'U'],
            'absences': [10, 20 , 35 , 2, 10],
            'FinalGrade': [30, 23, 2, 90, 10]
        }
        
        self.data_encoded = pd.DataFrame(data_encoded)
        self.data_scaled = pd.DataFrame(data_scaled)

        self.clustering = Clustering(self.data_encoded, self.data_scaled)  

    
    def test_Kprototypes(self):
        n_clusters = 2
        result = self.clustering.Kprototypes(n_clusters)
        
        # Vérifier si une colonne 'cluster' a été ajoutée et si elle contient bien les bons clusters
        self.assertIn("cluster", result.columns)
        self.assertEqual(len(result["cluster"].unique()), n_clusters)
    
    def test_analyse_Kprototypes(self):
        n_clusters = 3
        data_with_cluster = self.clustering.Kprototypes(n_clusters)
        
        # Vérifier si la méthode retourne un DataFrame et si les clusters sont analysés
        result = self.clustering.analyse_Kprototypes(data_with_cluster)
        self.assertTrue(isinstance(result, pd.DataFrame))
        self.assertTrue('FinalGrade' in result.columns)

if __name__ == '__main__':
    unittest.main()
