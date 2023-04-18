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


if __name__ == '__main__':
    unittest.main()
