import unittest
from project_compression.token_estimator import estimate_tokens

class TestTokenEstimator(unittest.TestCase):

    def test_estimate_tokens(self):
        text = "This is a sample text."
        method = "max"

        estimated_tokens = estimate_tokens(text, method)

        # Perform tests on the estimated_tokens
        # Add your assertions here to test if the token estimation was successful

if __name__ == '__main__':
    unittest.main()
