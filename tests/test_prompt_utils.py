import unittest
import os
from project_compression.prompt_utils import get_folder_structure, add_prefix_prompt, compress_data_with_chunking

class TestPromptUtils(unittest.TestCase):

    def test_get_folder_structure(self):
        test_dir_path = 'test_project'
        ignored_folders = ['.git']
        ignored_files = ['.DS_Store']
        folder_structure = get_folder_structure(test_dir_path, ignored_folders, ignored_files)
        self.assertTrue(isinstance(folder_structure, str))

    def test_add_prefix_prompt(self):
        prompt_template = "This is a test prompt."
        prefix = "This is a test prefix."
        suffix = "This is a test suffix."
        result = add_prefix_prompt(prompt_template, prefix, suffix)
        self.assertIn(prefix, result)
        self.assertIn(suffix, result)
        self.assertIn(prompt_template.strip(), result)

    def test_compress_data_with_chunking(self):
        compressed_data = "This is a sample compressed data."
        model = 'gpt-3.5-turbo'
        temperature = 0.7
        max_content_tokens = 10
        compressed_result = compress_data_with_chunking(compressed_data, model, temperature, max_content_tokens)
        self.assertTrue(isinstance(compressed_result, str))

if __name__ == '__main__':
    unittest.main()
