import os
from project_compression.token_estimator import estimate_tokens
from project_compression.openai_utils import compress_string

def get_folder_structure(folder_path, ignored_folders=[], ignored_files=[], ignored_extensions=[], prefix=''):
    """
    Returns a text representation of the folder structure for a given directory path.

    Args:
    - folder_path: A string representing the path to the directory.
    - ignored_folders: A list of folder names to ignore.
    - ignored_files: A list of file names to ignore.
    - ignored_extensions: A list of file extensions to ignore.
    - prefix: A string representing the prefix to add to the folder structure text.

    Returns:
    A string representing the text of the directory structure.
    """

    folder_structure = f'{prefix}{os.path.basename(folder_path)}/\n'
    prefix += '|   '
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isfile(item_path):
            if item.endswith(tuple(ignored_extensions)) or item in ignored_files:
                continue
            folder_structure += f'{prefix}|-- {item}\n'
        elif os.path.isdir(item_path):
            if item in ignored_folders:
                continue
            folder_structure += get_folder_structure(item_path, ignored_folders=ignored_folders, ignored_files=ignored_files, ignored_extensions=ignored_extensions, prefix=prefix)
            
    return folder_structure


def add_prefix_prompt(prompt_template, prefix, suffix):
    """
    Adds a prefix and suffix prompt to a given string.

    Args:
    - prompt_template: A string representing the text to which the prefix and suffix prompt should be added.
    - prefix: A string representing the prefix prompt to add.
    - suffix: A string representing the suffix prompt to add.

    Returns:
    A string representing the original text with the prefix and suffix prompts added.
    """
    prefix_prompt = f"{prefix}\n\n"
    suffix_prompt = f"\n\n{suffix}"
    return prefix_prompt + prompt_template.strip() + suffix_prompt

def compress_data_with_chunking(compressed_data, model, temperature, max_content_tokens):
    """
    Compresses the given data in chunks if it exceeds the maximum number of tokens allowed.

    Args:
    - compressed_data: str, the data to compress
    - model: str, the name of the OpenAI language model to use for compression
    - temperature: float, the temperature setting to use for the language model
    - max_content_tokens: int, the maximum number of tokens allowed for the compressed data

    Returns:
    - str, the compressed data
    """
    # estimate the number of tokens for the compressed data
    num_tokens = estimate_tokens(compressed_data)

    # if the number of tokens exceeds the maximum allowed, split the compressed data into chunks and compress each chunk separately
    if num_tokens > max_content_tokens:
        compressed_chunks = []
        current_chunk = ''
        for line in compressed_data.split('\n'):
            line_tokens = estimate_tokens(line)
            if len(current_chunk) + line_tokens > max_content_tokens:
                compressed_chunks.append(compress_string(current_chunk, model, temperature))
                current_chunk = line
            else:
                current_chunk += '\n' + line
        if current_chunk:
            compressed_chunks.append(compress_string(current_chunk, model, temperature))
        compressed_data = '\n'.join(compressed_chunks)
    else:
        compressed_data = compress_string(compressed_data, model, temperature)

    return compressed_data