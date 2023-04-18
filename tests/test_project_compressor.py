import unittest
from unittest.mock import patch
from project_compression.project_compression import ProjectCompressor
import os

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

    def test_save_compressed_data_to_file(self):
        compressed_data = {
            'file1': 'Compressed content 1',
            'file2': 'Compressed content 2'
        }
        output_file = 'compressed_data.txt'
        compressor = ProjectCompressor()
        compressor.save_compressed_data_to_file(compressed_data, output_file)

        self.assertTrue(os.path.exists(output_file))

        # Clean up - remove the output file
        os.remove(output_file)

if __name__ == '__main__':
    unittest.main()
