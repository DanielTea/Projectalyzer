import unittest
from project_compression.token_estimator import estimate_tokens

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
