from PyPDF2 import PdfMerger
import os

def pdf_searching(path):
    pdf_list = []
    for file in os.listdir(path):
        if file.endswith(".pdf"):
            full_path = os.path.join(path, file)
            pdf_list.append(full_path)
    pdf_list.sort(key=extract_chapter_number)
    print(pdf_list)
    return pdf_list

def extract_chapter_number(filename):
    return int(filename.split('chapter')[1].split('.')[0])

def datacamp_slides(pdf_list):
    merger = PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    dir_name = os.path.basename(path)
    output_file = os.path.join(path, f"{dir_name}.pdf")
    merger.write(output_file)
    merger.close()
    print(f"{dir_name}.pdf is created")
    return output_file

if __name__ == "__main__":
    path = input("Enter Path: \n")
    pdf_list = pdf_searching(path)
    datacamp_slides(pdf_list)
