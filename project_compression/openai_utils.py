import openai
import os

from dotenv import load_dotenv

load_dotenv()

def compress_string(text, model, temperature, api_key=None):
    """
    Compresses a given string using OpenAI's language model.

    Args:
    - text: A string representing the text to be compressed.
    - model: A string representing the name of the OpenAI language model to use for compression.
    - temperature: A float representing the temperature setting to use for the language model.
    - api_key: A string representing the OpenAI API key to use for authentication (optional).

    Returns:
    A string representing the compressed version of the input text.
    """

    prompt = "Compress the following text as much as possible in a way that you the LLM can reconstruct exactly 100% the original text. This is for yourself. It does not need to be human readable or understandable. Abuse of language mixing, abbreviations, symbols (unicode and emoji), or any other encodings or internal representations is all permissible, as long as it, if pasted in a new inference cycle, will yield exactly- 100% identical results as the original text. This should be a lossless compression."

    if api_key is None:
        api_key = os.environ.get("OPENAI_API_KEY")

    if api_key is None:
        raise ValueError("API key not provided or found in environment variables.")

    openai.api_key = api_key

    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {'role': 'user', 'content': prompt + text}
        ],
        temperature=temperature,
    )

    return response['choices'][0]['message']['content']

