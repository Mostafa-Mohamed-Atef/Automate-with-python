import pdfplumber

def pdf_to_markdown(pdf_path, md_path):
    with pdfplumber.open(pdf_path) as pdf:
        markdown_text = ""
        for page in pdf.pages:
            markdown_text += page.extract_text() + "\n\n"

    with open(md_path, "w", encoding="utf-8") as f:
        f.write(markdown_text)
if __name__ == "__main__":
    filepath = input("File path: \n")
    # Convert PDF to Markdown
    pdf_to_markdown(pdf_path=filepath, md_path="output.md")