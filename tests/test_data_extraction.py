import unittest
import pandas as pd
from data_extraction.extract_data import extract_data

class TestDataExtraction(unittest.TestCase):
    
    def test_extract_data(self):
        df = extract_data("data.csv")
        self.assertEqual(len(df), 100)
        self.assertIn("id", df.columns)
        self.assertIn("name", df.columns)
        self.assertIn("age", df.columns)

if __name__ == "__main__":
    unittest.main()
