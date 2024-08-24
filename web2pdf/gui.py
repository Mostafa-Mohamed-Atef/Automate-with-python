import ttkbootstrap as ttk
from tkinter import messagebox
import pdfkit

def Download():
    try:
        pdfkit.from_url(url.get(), f"{file_name.get()}.pdf")
        output.set('it should be done by now go check your file')
    except:
        messagebox.showerror('Invalid input', 'Your need to enter an equation!')

def clear():
    url_entry.delete(0, ttk.END)
    name_entry.delete(0, ttk.END)
    output_label.delete(0, ttk.END)

    url_entry.focus()


window = ttk.Window(themename='minty')
window.title("website to PDF")
window.geometry('600x400')

#variables
url = ttk.StringVar()
file_name = ttk.StringVar()
output = ttk.StringVar()

#widgets
input_frame = ttk.Frame(master=window,padding=50)
button_frame = ttk.Frame(master=window)
label = ttk.Label(master=input_frame,text='Enter URL')
url_entry = ttk.Entry(master=input_frame,justify='center',textvariable=url)
second_input_frame = ttk.Frame(master=window,padding=50)
file_label = ttk.Label(master=second_input_frame,text='Enter file name')
name_entry = ttk.Entry(master=second_input_frame,justify='center',textvariable=file_name)
clear_button = ttk.Button(master=window,text="\u232B",command=clear,padding=10)
download_button = ttk.Button(master=window,text="Download",command=Download,padding=10)
output_label = ttk.Label(master=window,textvariable=output,padding=10)

#packing widgets
input_frame.pack()
label.pack()
url_entry.pack(side='left')
url_entry.focus()
second_input_frame.pack()
file_label.pack()
name_entry.pack(side='left')
clear_button.pack()
button_frame.pack()
download_button.pack(pady=10)
output_label.pack()

window.mainloop()