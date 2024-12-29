import sys
import os
import unittest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from data_generation.generate_data import generate_data
from data_extraction.extract_data import extract_data
from data_transformation.transform_data import transform_data
from data_validation.validate_data import validate_data
from data_loading.store_data import store_data

def run_pipeline():
    try:
        raw_data_file = "data.csv"
        transformed_data_file = "transformed_data.csv"
        database_file = "dataops_pipeline.db"
        table_name = "transformed_data"

        # Phase d'extraction
        print("Starting data extraction...")
        extract_data(raw_data_file)
        print("Running tests for data extraction...")
        run_tests("tests.test_data_extraction")

        # Phase de validation
        print("Validating data...")
        validate_data(raw_data_file)
        print("Running tests for data validation...")
        run_tests("tests.test_data_validation")

        # Phase de transformation
        print("Transforming data...")
        transform_data(raw_data_file, transformed_data_file)
        print("Running tests for data transformation...")
        run_tests("tests.test_data_transformation")

        # Phase de chargement
        print("Storing transformed data into database...")
        store_data(transformed_data_file, database_file, table_name)
        print("Running tests for data loading...")
        run_tests("tests.test_data_loading")

        print("Pipeline executed successfully.")
    except Exception as e:
        print(f"Pipeline execution failed: {e}")

def run_tests(test_module):
    """
    Exécute un module de test spécifique.
    
    Args:
        test_module (str): Nom du module de test à exécuter (exemple : "tests.test_extraction").
    """
    suite = unittest.defaultTestLoader.loadTestsFromName(test_module)
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    if not result.wasSuccessful():
        raise Exception(f"Tests in {test_module} failed.")

if __name__ == "__main__":
    run_pipeline()
