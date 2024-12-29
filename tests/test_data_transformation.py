import unittest
import pandas as pd
from data_transformation.transform_data import transform_data

class TestDataTransformation(unittest.TestCase):

    def test_transform_data(self):
        transform_data("data.csv", "transformed_data.csv")
        df = pd.read_csv("transformed_data.csv")
        self.assertTrue((df["age"] >= 25).all())
        self.assertIn("tax", df.columns)
        self.assertTrue((df["tax"] > 0).all())

if __name__ == "__main__":
    unittest.main()
