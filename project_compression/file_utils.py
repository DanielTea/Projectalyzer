from project_compression.token_estimator import estimate_tokens

def read_file_content(file_path, encoding='utf-8'):
    """
    Reads the content of a file and returns it as a string.

    Args:
    - file_path: A string representing the path to the file.
    - encoding: A string representing the encoding to use when reading the file. Defaults to 'utf-8'.

    Returns:
    A string representing the content of the file.
    """
    with open(file_path, 'r', encoding=encoding) as f:
        content = f.read()
    return content

def save_chunks_to_files(compressed_data, base_filename='compressed_project_chunk'):
    
    for i, chunk in enumerate(compressed_data):
        with open(f"{base_filename}_{i}.txt", "w") as f:
            f.write(chunk)

    return len(compressed_data)



