from pdf2image import convert_from_path, convert_from_bytes
import os 

pages = convert_from_path('name.pdf')

for page in pages:
    page.save('output.jpg', 'JPEG')