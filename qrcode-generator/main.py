import qrcode
import tkinter as tk
import ttkbootstrap as ttk
import os

def generate():
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url.get())
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    
    # Create the full file path by combining path and file name
    full_path = os.path.join(path.get(), f'{file_name.get()}.jpg')
    
    # Save the image
    img.save(full_path)
    
    output.set(f"QR code saved to {full_path}")

def clear():
    url_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    path_entry.delete(0, tk.END)
    url_entry.focus()

# Initializing window
window = ttk.Window(themename='superhero')
window.title('QRCode Generator')
window.geometry('600x400')

# Declaring variables
url = ttk.StringVar()
file_name = ttk.StringVar()
path = ttk.StringVar()
output = ttk.StringVar()

# Creating frames
input_frame = ttk.Frame(master=window, padding=20)
second_input_frame = ttk.Frame(master=window, padding=20)
path_frame = ttk.Frame(master=window, padding=20)
button_frame = ttk.Frame(master=window, padding=20)

# Creating widgets
label = ttk.Label(master=input_frame, text='Enter URL')
url_entry = ttk.Entry(master=input_frame, justify='center', textvariable=url)

file_label = ttk.Label(master=second_input_frame, text='Enter file name')
name_entry = ttk.Entry(master=second_input_frame, justify='center', textvariable=file_name)

path_label = ttk.Label(master=path_frame, text='Enter path')
path_entry = ttk.Entry(master=path_frame, justify='center', textvariable=path)

clear_button = ttk.Button(master=button_frame, text="\u232B Clear", command=clear, padding=10)
download_button = ttk.Button(master=button_frame, text="Generate", command=generate, padding=10)
output_label = ttk.Label(master=window, textvariable=output, padding=10)

# Packing widgets with better alignment
input_frame.pack(pady=10)
label.pack(side='left', padx=5)
url_entry.pack(side='left', fill='x', expand=True, padx=5)

second_input_frame.pack(pady=10)
file_label.pack(side='left', padx=5)
name_entry.pack(side='left', fill='x', expand=True, padx=5)

path_frame.pack(pady=10)
path_label.pack(side='left', padx=5)
path_entry.pack(side='left', fill='x', expand=True, padx=5)

button_frame.pack(pady=20)
clear_button.pack(side='left', padx=5)
download_button.pack(side='left', padx=5)

output_label.pack(pady=20)

window.mainloop()
