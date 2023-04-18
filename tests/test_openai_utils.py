import unittest
from unittest.mock import patch
from project_compression.openai_utils import compress_string

class TestOpenAIUtils(unittest.TestCase):

    @patch("project_compression.openai_utils.openai.Completion.create")
    def test_compress_string(self, mock_completion_create):
        # Mock the response from the OpenAI API
        mock_completion_create.return_value.choices = [{"text": "Compressed text"}]

        text = "This is a sample text."
        model = 'gpt-3.5-turbo'
        temperature = 0.7
        compressed_text = compress_string(text, model, temperature)

        self.assertEqual(compressed_text, "Compressed text")

if __name__ == '__main__':
    unittest.main()
