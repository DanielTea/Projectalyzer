import argparse
import os
import yaml
from project_compression.project_compression import ProjectCompressor
from project_compression.file_utils import save_chunks_to_files
from project_compression.token_estimator import estimate_tokens

# create the parser object
parser = argparse.ArgumentParser(description='Compress a project directory and write it to a text file.')

# add arguments
parser.add_argument('--project', type=str, help='The path to the project directory.', required=True)
parser.add_argument('--prefix', type=str, help='The prefix prompt to add to the compressed output.', default="This is compressed text, in your own language. You should be able to decompress it because it's in your language. Here's what to decompress:")
parser.add_argument('--suffix', type=str, help='The suffix prompt to add to the compressed output.', default="Explain the decompressed content.")
parser.add_argument('--model', type=str, help='The OpenAI language model to use for compression.', default='gpt-3.5-turbo')
parser.add_argument('--temperature', type=float, help='The temperature setting to use for the language model.', default=0.4)
parser.add_argument('--config', type=str, help='The path to the configuration file for folders and files to ignore during compression.', default='config.yml')
parser.add_argument('--max_content_tokens', type=int, help='The maximum number of content tokens allowed for each chunk of compressed data.', default=4000)
parser.add_argument('--api_key', type=str, help='The OpenAI API key. If not provided, it will be read from the environment variable OPENAI_API_KEY.')
parser.add_argument('--save', action='store_true', help='Save compressed files to text files.', default=True)



# parse the arguments
args = parser.parse_args()

# assign arguments to variables
project_folderpath = args.project
prefix = args.prefix
suffix = args.suffix
model = args.model
temperature = args.temperature
config_file_path = args.config
max_content_tokens = args.max_content_tokens

def read_config_file(config_file_path):
    with open(config_file_path) as f:
        config = yaml.safe_load(f)
    return config

config = read_config_file(config_file_path)

ignored_folders = config.get('ignored_folders', [])
ignored_files = config.get('ignored_files', [])
ignored_extensions = config.get('ignored_extensions', [])

openai_api_key = args.api_key if args.api_key else os.environ.get('OPENAI_API_KEY')
if not openai_api_key:
    raise ValueError("No OpenAI API key provided or found in the environment variable OPENAI_API_KEY.")

# Create the compressor object
compressor = ProjectCompressor(model=model, temperature=temperature, max_content_tokens=max_content_tokens, prefix=prefix, suffix=suffix, api_key=openai_api_key, config_file_path=config_file_path)

compressed_data = compressor.compress_project(project_folderpath)

total_tokens = sum([estimate_tokens(chunk) for chunk in compressed_data])
print(f"Estimated total tokensize of compressed_data: {total_tokens}")

if args.save:
    num_chunks = save_chunks_to_files(compressed_data)
    print(f"{num_chunks} chunk(s) saved.")