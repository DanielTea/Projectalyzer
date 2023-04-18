import openai
import os
import yaml
from .openai_utils import compress_string
from .token_estimator import estimate_tokens
from .file_utils import read_file_content
from .prompt_utils import add_prefix_prompt, get_folder_structure

class ProjectCompressor:
    def __init__(self, model='gpt-3.5-turbo', temperature=0.7, max_content_tokens=4000, prefix="", suffix="", config_file_path=None, api_key=None):
        self.model = model
        self.temperature = temperature
        self.max_content_tokens = max_content_tokens
        self.prefix = prefix
        self.suffix = suffix
        self.config_file_path = config_file_path
        self.api_key = api_key

        if self.api_key:
            os.environ["OPENAI_API_KEY"] = self.api_key

    def read_config_file(self):
        if not self.config_file_path:
            return {'ignored_folders': [], 'ignored_files': [], 'ignored_extensions': []}

        with open(self.config_file_path) as f:
            config = yaml.safe_load(f)
        return config

    def compress_project(self, project_folderpath):
        print(f"Compressing project at {project_folderpath}...")
        folder_structure = get_folder_structure(project_folderpath, **self.read_config_file())

        print(folder_structure)

        estimated_tokens = estimate_tokens(folder_structure)
        print(f"ESTIMATED TOKEN LENGTH: {estimated_tokens}")

        if estimated_tokens > self.max_content_tokens:
            comp_folder_structure = "AMOUNT OF PATHS AND FILES TOO MANY TO BE ANALYSED. ASK FOR MORE INFORMATION WHEN FOLDERSTRUCTURE IS NEEDED."
            print("FOLDER STRUCTURE TOO LARGE TO BE ANALYSED. ASK FOR MORE INFORMATION WHEN NEEDED.")

        else:
            comp_folder_structure = compress_string(folder_structure, self.model, self.temperature, self.api_key)
            print("Folder structure compressed successfully!")

        compressed_content = {}
        for root, dirs, files in os.walk(project_folderpath):
            for file in files:
                file_path = os.path.join(root, file)
                file_ext = os.path.splitext(file_path)[1]
                if file_ext in self.read_config_file().get('ignored_extensions', []):
                    continue
                if any(ignored_file in file_path for ignored_file in self.read_config_file().get('ignored_files', [])):
                    continue
                if any(ignored_folder in file_path for ignored_folder in self.read_config_file().get('ignored_folders', [])):
                    continue

                content = read_file_content(file_path)
                estimated_tokens = estimate_tokens(content)

                if estimated_tokens > self.max_content_tokens:
                    content = "COMPRESSION OUTPUT: FILE TOO LARGE TO BE ANALYSED. ASK FOR MORE INFORMATION WHEN CONTENT OF FILE IS NEEDED."
                    print("FILE TOO MANY TOKEN TO BE ANALYSED. IGNORED.")

                comp_content = compress_string(content, self.model, self.temperature, self.api_key)
                compressed_content[file_path] = comp_content
                print(f"ESTIMATED TOKEN LENGTH: {estimated_tokens}")
                print(f"{file_path} compressed successfully!")
                
        prompt_template = f"This is the compressed folder and file structure of the project: {comp_folder_structure}\n"

        chunks = []
        current_chunk = ''
        for file_path, comp_content in compressed_content.items():
            estimated_tokens = estimate_tokens(read_file_content(file_path))
            line = f"This is the compressed content of {file_path} with an estimated decompressed token length of {estimated_tokens}: {comp_content}\n"
            tmp_chunk = self.prefix +"\n"+ prompt_template + current_chunk + line + self.suffix
            if estimate_tokens(tmp_chunk) > self.max_content_tokens:
                chunks.append(tmp_chunk)
                current_chunk = ''

            current_chunk += line
        
        if current_chunk:
            final_chunk = self.prefix +"\n"+ prompt_template + current_chunk + line + self.suffix
            chunks.append(final_chunk)

        for i, chunk in enumerate(chunks):
            page_string = f"THIS IS PART {i} OF {len(chunks)}.\n"
            if isinstance(chunk, tuple):
                chunk = chunk[0]
            chunks[i] = page_string + chunk

        print("Project compressed successfully!")
                
        return chunks

