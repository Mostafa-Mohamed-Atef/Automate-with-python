import os
import PyPDF2
from typing import List, Tuple

def search_pdf(pdf_path: str, search_term: str) -> List[Tuple[int, str]]:
    """
    Search for a term in a PDF file and return matching pages with context
    
    Args:
        pdf_path: Path to the PDF file
        search_term: Term to search for
        
    Returns:
        List of tuples containing (page_number, matching_text)
    """
    matches = []
    try:
        with open(pdf_path, 'rb') as file:
            # Create PDF reader object
            pdf_reader = PyPDF2.PdfReader(file)
            
            # Search through each page
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text = page.extract_text().lower()
                
                if search_term.lower() in text:
                    # Get some context around the match
                    matches.append((page_num + 1, text))
                    
    except Exception as e:
        print(f"Error reading {pdf_path}: {str(e)}")
        
    return matches

def search_directory(directory: str, search_term: str) -> None:
    """
    Search all PDF files in a directory for a specific term
    
    Args:
        directory: Path to directory containing PDF files
        search_term: Term to search for
    """
    # Check if directory exists
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist!")
        return
        
    # Get all PDF files in directory
    pdf_files = [f for f in os.listdir(directory) if f.lower().endswith('.pdf')]
    
    if not pdf_files:
        print(f"No PDF files found in '{directory}'")
        return
        
    print(f"Searching for '{search_term}' in {len(pdf_files)} PDF files...\n")
    
    # Search each PDF file
    for pdf_file in pdf_files:
        pdf_path = os.path.join(directory, pdf_file)
        matches = search_pdf(pdf_path, search_term)
        
        if matches:
            print(f"\nFound matches in '{pdf_file}':")
            for page_num, context in matches:
                print(f"- Page {page_num}")

def main():
    # Set up argument parser
    # parser = argparse.ArgumentParser(description='Search for text in PDF files')
    # parser.add_argument('directory', help='Directory containing PDF files')
    # parser.add_argument('search_term', help='Term to search for')
    
    # Parse arguments
    # args = parser.parse_args()
    path = input("Enter Path: \n")
    term = input("Enter your search: \n")
    # Perform search
    search_directory(path, term)

if __name__ == "__main__":
    main()
