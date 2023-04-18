# 🚀 Projectalyzer

🔍 Projectalyzer is a Python script that compresses a project directory and writes the compressed data to a text file using OpenAI's language model.

## How It Works

Projectalyzer works in the following way:

1. Use the `get_folder_structure(folder_path, prefix='')` function to get a text representation of the folder structure for the project directory.
2. Compress the `folder_structure` string using OpenAI's language model to create `comp_folder_structure`.
3. Append to `prompt_template` the following text: "This is the compressed folder and file structure of the project: <comp_folder_structure>".
4. Iterate through every file in the project directory (excluding the file types in `excepted_filetypes`) to get the content of the file.
5. Compress the `content_of_file` string using OpenAI's language model to create `comp_content_of_file`.
6. Append to `prompt_template` the following text: "This is the compressed content of <file_path+file_name>: <comp_content_of_file>".
7. Save `prompt_template` to a text file(s) named `compressed_project_chunk_i.txt` in the current working directory.


## Usage

1. Install the required packages by running `pip install -r requirements.txt`.
2. Create a copy of the `.env.template` file named `.env` and replace `<your_api_key_here>` with your OpenAI API key.
3. Navigate to the project directory in the terminal.
4. Run the command `python main.py --project /path/to/project`.
5. Textfiles `compressed_project_chunk_i.txt` with the compressed project, as prompt is created in the projectalyzer directory.
6. Use the content of `compressed_project_chunk_i.txt` as first prompt to add all necessary project/directory info for the GPT Agent to work.

## Arguments

- `--project`: The path to the project directory. (Required)
- `--prefix`: The prefix prompt to add to the compressed output. Defaults to "This is compressed text, in your own language. You should be able to decompress it because it's in your language. Here's what to decompress:".
- `--suffix`: The suffix prompt to add to the compressed output. Defaults to "Explain the decompressed content.".
- `--model`: The OpenAI language model to use for compression. Defaults to "gpt-3.5-turbo".
- `--temperature`: The temperature setting to use for the language model. Defaults to 0.2.
- `--config`: The path to the configuration file for folders and files to ignore during compression. Defaults to "config.yml".
- `--max_content_tokens`: The maximum number of content tokens allowed for each chunk of compressed data. Defaults to 4000.

## Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key. (Required)

## Configuration File

The `config.yml` file specifies a list of folders and files to ignore during compression. The file should be in the following format:

```
ignored_folders:
  - .history
  - .git
  - __pycache__

ignored_files:
  - .env
  - old_projectanalyzer.py

ignored_extensions:
  - .pdf
  - .exe
  - .xlsx
  - .pyc
  - .txt
  - .png
```

Folders and files specified in this file will be excluded from the compressed output.

## Why Projectalyzer?

The goal of this project is to feed a large language model (LLM) compressed information about a software project so that the LLM can understand the whole project, including each file and folder structure. 🤖

## License

This project is licensed under the MIT License - see the