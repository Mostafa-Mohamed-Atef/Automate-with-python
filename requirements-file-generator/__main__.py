import os
import re
import sys
from importlib.metadata import packages_distributions


def find_python_files(directory):
    """Recursively find all .py files in the given directory."""
    python_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))
    return python_files


def extract_libraries(file_path):
    """Extract library imports from a Python file."""
    libraries = set()
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                # Match import statements (e.g., import x or from x import y)
                match = re.match(r'^\s*(?:import|from)\s+([\w_\.]+)', line)
                if match:
                    libraries.add(match.group(1).split('.')[0])  # Extract the root module
    except Exception as e:
        print(f"Error reading {file_path}: {e}", file=sys.stderr)
    return libraries


def map_to_packages(libraries):
    """Map imported libraries to actual package names."""
    distributions = packages_distributions()
    mapped_packages = set()
    for lib in libraries:
        # Check if the library maps to a distribution
        if lib in distributions:
            mapped_packages.update(distributions[lib])
        else:
            # Assume the library name is the package name if not mapped
            mapped_packages.add(lib)
    return mapped_packages


def generate_requirements(directory, output_file):
    """Generate a requirements.txt file based on imported libraries in .py files."""
    python_files = find_python_files(directory)
    all_libraries = set()

    for file_path in python_files:
        libraries = extract_libraries(file_path)
        all_libraries.update(libraries)

    # Map libraries to actual package names
    mapped_packages = map_to_packages(all_libraries)

    # Write packages to requirements.txt
    with open(output_file, "w") as file:
        for package in sorted(mapped_packages):
            file.write(f"{package}\n")
    print(f"Requirements written to {output_file}")


# Prompt user for directory path and generate requirements file
directory = input("Enter directory path:\n").strip()
if not os.path.isdir(directory):
    print("Invalid directory path. Please try again.")
else:
    generate_requirements(directory, os.path.join(directory, "requirements.txt"))
