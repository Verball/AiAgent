import os
from google.genai import types

MAX_CHARS = 10000

def get_files_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.join(working_directory, file_path)
    if not abs_file_path:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or it is not a regular file: "{file_path}"'
    
    with open(abs_file_path, "r") as f:
        try:
            file_content_string = f.read(MAX_CHARS)
            if sum(len(word) for word in file_content_string) == 10000:
                file_content_string += f"... File {file_path} truncated at 10000 characters"
            return file_content_string
        except Exception as e:
            return f"Error: Unable to retrive: {e}"
        
    
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Reads and returns the first {MAX_CHARS} characters of the content from a specified file within the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file whose content should be read, relative to the working directory.",
            ),
        },
        required=["file_path"],
    ),
)