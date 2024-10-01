from pdf2image import convert_from_path, convert_from_bytes
from fpdf import FPDF
import os 
import img2pdf
from PIL import Image
from pathlib import Path
        
def pdf_to_img(file, file_name):
    pages = convert_from_path(file)
    for page in pages:   
        page.save(f'{file_name}.jpg', 'JPEG')

def img_to_pdf(file, file_name):
    image = Image.open(file)
    pdf = img2pdf.convert(image.filename)
    with open(f'{file_name}.pdf', 'wb') as f:  # Save the PDF
        f.write(pdf)  # Write the PDF data to the file


for file in os.listdir('pdf2image'):
    if file.endswith(('.jpg','.jpeg', '.png')):
        file_name = Path(file).stem
        img_to_pdf(os.path.join('pdf2image', file), file_name)
    elif file.endswith('.pdf'):
        file_name = Path(file).stem
        pdf_to_img(os.path.join('pdf2image', file), file_name)

print(f"{file_name} is Done")

