import os
import re
import sys
from importlib.metadata import packages_distributions

def find_python_files(directory):
    """Recursively find all .py files in the given directory."""
    python_files = []
    for folder in os.listdir(directory):
            try:
                file_path = os.path.join(directory, folder)
                for file in os.listdir(folder):
                    if file.endswith(".py"):
                        python_files.append(os.path.join(file_path, file))
            except:
                continue
    return python_files

def extract_libraries(file_path):
    """Extract library imports from a Python file."""
    libraries = set()
    with open(file_path, "r") as file:
        for line in file:
            # Match import statements (e.g., import x or from x import y)
            match = re.match(r'^\s*(import|from)\s+([a-zA-Z0-9_]+)', line)
            if match:
                libraries.add(match.group(2))
    return libraries

def filter_builtin_libraries(libraries):
    """Filter out built-in libraries."""
    # Retrieve installed third-party packages in the environment
    installed_distributions = {pkg for pkg in packages_distributions().keys()}
    
    # Collect only third-party libraries
    third_party_libs = {lib for lib in libraries if lib in installed_distributions}
    return third_party_libs

def generate_requirements(directory, output_file):
    """Generate a requirements.txt file based on imported libraries in .py files."""
    python_files = find_python_files(directory)
    all_libraries = set()
    
    for file_path in python_files:
        libraries = extract_libraries(file_path)
        all_libraries.update(libraries)
    
    # Filter out built-in libraries
    # third_party_libs = filter_builtin_libraries(all_libraries)
    
    # Write libraries to requirements.txt
    with open(output_file, "w") as file:
        for lib in sorted(all_libraries):
            file.write(f"{lib}\n")
    print(f"Requirements written to {output_file}")

# Prompt user for directory path and generate requirements file
directory = input("Enter dir path:\n")
generate_requirements(directory, os.path.join(directory, "requirements.txt"))
