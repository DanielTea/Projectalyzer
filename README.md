# 🚀 Projectalyzer

Projectalyzer is a command-line tool that analyzes the contents of a software project directory and generates a report detailing various statistics and information about the project. 🕵️‍♀️

## Usage

1. Install the required packages by running `pip install -r requirements.txt`.
2. Create a copy of the `.env.template` file named `.env` and replace `<your_api_key_here>` with your OpenAI API key.
3. Navigate to the project directory in the terminal.
4. Run the command `python projectalyzer.py --project /path/to/project`.

## Arguments

- `--project`: The path to the software project directory. (Required)

## Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key. (Required)

## Why Projectalyzer?

The goal of this project is to feed a large language model (LLM) compressed information about a software project so that the LLM can understand the whole project, including each file and folder structure. 🤖

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
