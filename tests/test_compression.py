import unittest
from project_compression.project_compression import ProjectCompressor

class TestCompression(unittest.TestCase):

    def test_compression(self):
        # Set up the necessary parameters for testing
        project_folderpath = "test_project"
        excepted_filetypes = ['.pdf', '.exe', '.xlsx', '.pyc', '.txt', '.png', '.env', '.history']

        # Initialize the ProjectCompressor object
        compressor = ProjectCompressor(project_folderpath, excepted_filetypes)

        # Compress the project
        compressed_data = compressor.compress_project()

        # Perform tests on the compressed_data
        # Add your assertions here to test if the compression was successful

if __name__ == '__main__':
    unittest.main()

