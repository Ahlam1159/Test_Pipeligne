import unittest
import sqlite3
import pandas as pd
from data_loading.store_data import store_data

class TestDataLoading(unittest.TestCase):

    def test_store_data(self):
        store_data("transformed_data.csv", "dataops_pipeline.db", "transformed_data")
        
        # Vérifier si la table existe dans la base de données
        conn = sqlite3.connect("dataops_pipeline.db")
        query = "SELECT name FROM sqlite_master WHERE type='table' AND name='transformed_data';"
        result = conn.execute(query).fetchall()
        conn.close()

        self.assertEqual(len(result), 1)

if __name__ == "__main__":
    unittest.main()
