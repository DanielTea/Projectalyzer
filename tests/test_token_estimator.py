import unittest
from project_compression.token_estimator import estimate_tokens
import os

# Get the absolute path of the current file
current_file_path = os.path.abspath(__file__)

# Get the path of the "tests" folder
tests_folder_path = os.path.dirname(current_file_path)

# Get the path of the "test_data" folder
test_data_folder_path = os.path.join(tests_folder_path, 'test_data')

# Get the path of the "test_project" folder
test_project_folder_path = os.path.join(test_data_folder_path, 'test_project')

class TestTokenEstimator(unittest.TestCase):

    def test_estimate_tokens(self):
        text = "This is a sample text."
        method = "max"
        estimated_tokens = estimate_tokens(text, method)
        self.assertTrue(isinstance(estimated_tokens, int))

    def test_estimate_tokens_invalid_method(self):
        text = "This is a sample text."
        method = "invalid_method"
        result = estimate_tokens(text, method)
        self.assertEqual(result, "Invalid method. Use 'average', 'words', 'chars', 'max', or 'min'.")

if __name__ == '__main__':
    unittest.main()
