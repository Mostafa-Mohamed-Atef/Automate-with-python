import pdfkit

url = input("Your link: \n")
file_name = input("Enter your file name: \n")
pdfkit.from_url(url, f"{file_name}.pdf")
print('Done')