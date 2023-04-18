import unittest
from project_compression.token_estimator import estimate_tokens

class TestTokenEstimator(unittest.TestCase):

    def test_estimate_tokens(self):
        text = "This is a sample text."
        expected_token_count = 6  # 6 words

        token_count = estimate_tokens(text)
        self.assertEqual(token_count, expected_token_count)

    def test_estimate_tokens_with_empty_string(self):
        text = ""
        expected_token_count = 0

        token_count = estimate_tokens(text)
        self.assertEqual(token_count, expected_token_count)

if __name__ == '__main__':
    unittest.main()
