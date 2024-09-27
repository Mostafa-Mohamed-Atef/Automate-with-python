from pdf2image import convert_from_path, convert_from_bytes
import os 

pages = convert_from_path('name.pdf')

for page in pages:
    page.save('output.jpg', 'JPEG')
#EDIT THIS FOR CONVERTING IMG TO PDF
import img2pdf
with open("output.pdf", "wb") as file:
   file.write(img2pdf.convert([i for i in os.listdir('path to image') if i.endswith(".jpg")]))