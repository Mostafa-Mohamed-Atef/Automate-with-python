import pdfkit
import os 

# List HTML files
html_files = [file for file in os.listdir("PDF-Generator") if file.endswith("html")]
for file in html_files:
    print(file, end='\n')

# Get user input
file_name = input("Enter file name: \n")

# Check if the file exists
if file_name in html_files:
    pdfkit.from_file(f"PDF-Generator/{file_name}", f"{file_name}.pdf")
    print("Done")
else:
    print(f"Error: {file_name} does not exist in the PDF-Generator directory.")