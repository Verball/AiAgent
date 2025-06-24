from functions.get_files_info import get_files_info
from functions.get_files_content import get_files_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

def main():
    
    result = get_files_content("calculator","main.py")
    print(result)

    result = write_file("calculator", "main.txt", 'hello')
    print(result)

    result = run_python_file("calculator", "main.py")
    print(result)

    result = get_files_info("calculator", "pkg")
    print(result)

    
if __name__ == "__main__":
    main()