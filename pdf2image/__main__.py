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
    print(f"{file_name} is Done")

def img_to_pdf(file, file_name):
    image = Image.open(file)
    if image.mode in ("RGBA", "LA") or (image.mode == "P" and "transparency" in image.info):
        # Convert the image to RGB (remove alpha channel)
        image = image.convert("RGB")
    pdf = img2pdf.convert(image.filename)
    with open(f'{file_name}.pdf', 'wb') as f:  # Save the PDF
        f.write(pdf)  # Write the PDF data to the file
    print(f"{file_name} is Done")

if __name__=="__main__":
    path = input("Enter path: \n")
    files = os.listdir(path)
    for file in files:
        full_path = os.path.join(path, file)
        if file.endswith(('.jpg','.jpeg', '.png')):
            file_name = Path(file).stem
            img_to_pdf(full_path, file_name)
        elif file.endswith('.pdf'):
            file_name = Path(file).stem
            pdf_to_img(full_path, file_name)


