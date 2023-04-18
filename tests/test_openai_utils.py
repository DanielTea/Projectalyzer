import unittest
from unittest.mock import patch
from project_compression.openai_utils import compress_string
import os

# Get the absolute path of the current file
current_file_path = os.path.abspath(__file__)

# Get the path of the "tests" folder
tests_folder_path = os.path.dirname(current_file_path)

# Get the path of the "test_data" folder
test_data_folder_path = os.path.join(tests_folder_path, 'test_data')

# Get the path of the "test_project" folder
test_project_folder_path = os.path.join(test_data_folder_path, 'test_project')

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
