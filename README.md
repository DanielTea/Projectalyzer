# 🚀 Projectalyzer

Projectalyzer is a command-line tool that analyzes the contents of a software project directory and generates a report detailing various statistics and information about the project. 🕵️‍♀️

## Usage

1. Install the required packages by running `pip install -r requirements.txt`.
2. Create a copy of the `.env.template` file named `.env` and replace `<your_api_key_here>` with your OpenAI API key.
3. Navigate to the project directory in the terminal.
4. Run the command `python projectalyzer.py --project /path/to/project`.
5. A textfile `'compressed_project_prompt.txt'` with the compressed project, as prompt is created in the projectalyzer directory.

## Arguments

- `--project`: The path to the software project directory. (Required)

Projectalyzer has the following optional arguments:

- `--prefix`: The prefix prompt to add to the compressed output. Defaults to "This is compressed text, in your own language. You should be able to decompress it because it's in your language. Here's what to decompress:".
- `--suffix`: The suffix prompt to add to the compressed output. Defaults to "Explain the decompressed content.".
- `--model`: The OpenAI language model to use for compression. Defaults to "gpt-3.5-turbo".
- `--temperature`: The temperature setting to use for the language model. Defaults to 0.3. (less creates larger but more detailed compressions)
- `--excepted_filetypes`: A list of file extensions to exclude from compression. Defaults to [".pdf", ".exe", ".xlsx", ".pyc", ".txt", ".png"].

## Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key. (Required)

## Why Projectalyzer?

The goal of this project is to feed a large language model (LLM) compressed information about a software project so that the LLM can understand the whole project, including each file and folder structure. 🤖

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
