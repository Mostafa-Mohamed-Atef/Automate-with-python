import subprocess
import os

def load_files(repo_directory):
    result = {}
    
    for dirpath, dirnames, filenames in os.walk(repo_directory):
        for filename in filenames:
            if filename.endswith('.py') and filename in ["__main__.py", "gui.py"]:
                descriptive_name = os.path.basename(dirpath).replace("-", " ")
                if "gui" in filename.lower():
                    descriptive_name += " with GUI"
                result[descriptive_name] = os.path.join(dirpath, filename)
    
    return result

def get_user_choice(indexed_files):
    try:
        choice = int(input("What do you want to run: \n"))
        if 1 <= choice <= len(indexed_files):
            return choice
        else:
            print(f"Error: Choice {choice} is out of range.")
            return None
    except ValueError:
        print("Error: Invalid input. Please enter a number.")
        return None

def run_file(file_path):
    directory = os.path.dirname(file_path)
    if os.path.exists(file_path):
        print("Seconds please...")
        result = subprocess.run(["python3", file_path], cwd=directory)
        if result.returncode == 0:
            print("Execution successful!")
        else:
            print("Execution failed!")
            print(result.stderr)
    else:
        print(f"Error: The file '{file_path}' does not exist.")

def main():
    os.chdir('..')
    repo_directory = os.getcwd()
    files = load_files(repo_directory)
    if not files:
        return

    indexed_files = list(enumerate(files.keys(), start=1))
    print(f'Here are your files: {indexed_files}')

    choice = get_user_choice(indexed_files)
    if choice is None:
        return

    choosed_file = indexed_files[choice - 1][1]
    file_path = files.get(choosed_file)

    if file_path:
        run_file(file_path)
    else:
        print(f"Error: '{choosed_file}' is not a valid choice.")

if __name__ == "__main__":
    main()
