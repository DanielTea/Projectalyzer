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
