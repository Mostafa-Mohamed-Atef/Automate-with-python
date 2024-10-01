from pdf2image import convert_from_path, convert_from_bytes
from fpdf import FPDF
import os 

        
def pdf_to_img(file, file_name):
    pages = convert_from_path(file)
    for page in pages:   
        page.save(f'{file_name}.jpg', 'JPEG')
#EDIT THIS FOR CONVERTING IMG TO PDF
def img_to_pdf(file, file_name):
    pdf = FPDF()
    pdf.add_page()
    pdf.image(file)
    pdf.output(f"{file_name}.pdf")


for file in os.listdir('pdf2image'):
    if file.endswith(('.jpg', '.png')):
        file_name = file.title()
        img_to_pdf(os.path.join('pdf2image', file), file_name)
    elif file.endswith('.pdf'):
        file_name = file.title()
        pdf_to_img(os.path.join('pdf2image', file), file_name)

print(f"{file_name} is Done")

import AsposePDFPythonWrappers as apw
import os
import os.path
from PIL import Image

# Set the directory path for the data files
dataDir = os.path.join(os.getcwd(), "samples")

# Set the input file path
input_file = os.path.join(dataDir, "sample.jpg")

# Set the output file path
output_file = os.path.join(dataDir, "results", "jpg-to-pdf.pdf")

# Open the input image file using PIL library
pil_img = Image.open(input_file)

# Get the width and height of the image
width, height = pil_img.size

# Create a new Document instance using AsposePDFPythonWrappers library
document = apw.Document()

# Create a new Image instance using AsposePDFPythonWrappers library
image = apw.Image()

# Set the file path of the image
image.file = input_file

# Set the fixed height and width of the image
image.fix_height = height
image.fix_width = width

# Add a new page to the document
page = document.pages.add()

# Add the image to the page
page.paragraphs.add(image)

# Save the document to the output file path
document.save(output_file)
