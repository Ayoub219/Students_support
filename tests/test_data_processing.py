import unittest
import pandas as pd
import numpy as np
from src.data_processing import PretraitementsDonnees

class TestPretraitementsDonnees(unittest.TestCase):
    def setUp(self):
        self.data = pd.DataFrame({
            'sex': ['F', 'M', 'F', 'M', 'F'],
            'age': [15, 17, 16, 18, 20],
            'address': ['R', 'R', 'U', 'R', 'U'],
            'FinalGrade': [30, 23, 2, 90, 10]
        })
        self.pretraitement = PretraitementsDonnees(self.data)

    def test_encodage_var_categorielles(self):
        categorical_columns = ['sex', 'address']
        encoded_df = self.pretraitement.encodage_var_categorielles(categorical_columns)
        # Vérifie que les colonnes ont été encodées et contiennent des entiers
        self.assertTrue(encoded_df['sex'].dtype == np.int8)
        self.assertTrue(encoded_df['address'].dtype == np.int8)

    def test_scale_data(self):
        categorical_columns = ['sex', 'address']
        encoded_df = self.pretraitement.encodage_var_categorielles(categorical_columns)
        numerical_columns = ['age', 'FinalGrade']
        scaled_df = self.pretraitement.scale_data(encoded_df, numerical_columns)
        # Vérifie que les colonnes numériques sont bien standardisées
        assert abs(scaled_df['age'].mean()) < 1e-2  
        assert abs(scaled_df['FinalGrade'].mean()) < 1e-2  

if __name__ == '__main__':
    unittest.main()
