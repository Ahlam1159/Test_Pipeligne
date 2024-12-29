import unittest
from data_validation.validate_data import validate_data

class TestDataValidation(unittest.TestCase):

    def test_validate_data(self):
        try:
            validate_data("data.csv")
        except ValueError as e:
            self.fail(f"Validation failed: {e}")

if __name__ == "__main__":
    unittest.main()
