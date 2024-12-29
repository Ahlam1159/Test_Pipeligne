import unittest
from pipelines.etl_pipeline import run_pipeline

class TestPipeline(unittest.TestCase):

    def test_pipeline(self):
        try:
            run_pipeline()
        except Exception as e:
            self.fail(f"Pipeline failed: {e}")

if __name__ == "__main__":
    unittest.main()
