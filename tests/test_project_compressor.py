import unittest
from unittest.mock import patch
from project_compression.project_compression import ProjectCompressor
import os

# Get the absolute path of the current file
current_file_path = os.path.abspath(__file__)

# Get the path of the "tests" folder
tests_folder_path = os.path.dirname(current_file_path)

# Get the path of the "test_data" folder
test_data_folder_path = os.path.join(tests_folder_path, 'test_data')

# Get the path of the "test_project" folder
test_project_folder_path = os.path.join(test_data_folder_path, 'test_project')

class TestProjectCompressor(unittest.TestCase):

    @patch("project_compression.project_compression.compress_string")
    def test_compress_project(self, mock_compress_string):
        # Mock the compress_string function
        mock_compress_string.return_value = "Compressed content"

        project_folderpath = "test_project"
        compressor = ProjectCompressor()

        compressed_data = compressor.compress_project(project_folderpath)
        self.assertTrue(isinstance(compressed_data, dict))

    @patch("project_compression.project_compression.compress_string")
    def test_compress_project_with_invalid_path(self, mock_compress_string):
        # Mock the compress_string function
        mock_compress_string.return_value = "Compressed content"

        project_folderpath = "invalid_project_path"
        compressor = ProjectCompressor()

        with self.assertRaises(FileNotFoundError):
            compressor.compress_project(project_folderpath)


if __name__ == '__main__':
    unittest.main()
