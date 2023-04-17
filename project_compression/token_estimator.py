def estimate_tokens(text, method="max"):
    """
    Estimates the number of tokens in a given text using different methods.

    Args:
    - text: A string representing the text to be tokenized.
    - method: A string representing the estimation method. Can be "average", "words", "chars", "max", "min". Defaults to "max".

    Returns:
    An integer representing the estimated number of tokens in the input text.
    """

    word_count = len(text.split())
    char_count = len(text)

    tokens_count_word_est = float(word_count) / 0.75
    tokens_count_char_est = float(char_count) / 4.0

    if method == "average":
        output = (tokens_count_word_est + tokens_count_char_est) / 2
    elif method == "words":
        output = tokens_count_word_est
    elif method == "chars":
        output = tokens_count_char_est
    elif method == 'max':
        output = max(tokens_count_word_est, tokens_count_char_est)
    elif method == 'min':
        output = min(tokens_count_word_est, tokens_count_char_est)
    else:
        return "Invalid method. Use 'average', 'words', 'chars', 'max', or 'min'."

    return int(output)
