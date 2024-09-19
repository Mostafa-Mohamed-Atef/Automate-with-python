import ttkbootstrap as ttk
from tkinter import messagebox
from sympy import *

def calculate():
    try:
        w = float(weight.get())
        h = float(height.get())/100
        
        if w <= 0 or h <= 0:
            raise ValueError("Weight and height must be positive numbers")
        
        bmi = w / (h ** 2)
        bmi_rounded = round(bmi, 2)
        
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 25:
            category = "Normal"
        elif 25 <= bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"
        
        output.set(f"BMI: {bmi_rounded} - {category}")
    except ValueError as e:
        messagebox.showerror('Invalid input', str(e))
    except ZeroDivisionError:
        messagebox.showerror('Invalid input', 'Height cannot be zero')

def clear():
    weight_entry.delete(0, ttk.END)
    weight_entry.focus()


# Set up the main window
window = ttk.Window(themename='superhero')
window.title("BMI")
window.geometry('400x250')
window.resizable(False, False)

# Variables
weight = ttk.StringVar()
height = ttk.StringVar()
output = ttk.StringVar()  # Changed to StringVar for better display of solutions

# Input Frame
input_frame = ttk.Frame(master=window, padding=(20, 10))
input_frame.pack(fill='x')

weight_label = ttk.Label(master=input_frame, text='Enter your Weight:', anchor='w')
weight_label.pack(fill='x')

weight_entry = ttk.Entry(master=input_frame, textvariable=weight, justify='center')
weight_entry.pack(fill='x', pady=5)
weight_entry.focus()

height_label = ttk.Label(master=input_frame, text='Enter your Height:', anchor='w')
height_label.pack(fill='x')

height_entry = ttk.Entry(master=input_frame, textvariable=height, justify='center')
height_entry.pack(fill='x', pady=5)

# Button Frame
button_frame = ttk.Frame(master=window, padding=(20, 10))
button_frame.pack(fill='x')

clear_button = ttk.Button(master=button_frame, text="\u232B Clear", command=clear)
clear_button.pack(side='left', padx=5)

cal_button = ttk.Button(master=button_frame, text="Calculate", command=calculate)
cal_button.pack(side='right', padx=5)

# Output Frame
output_frame = ttk.Frame(master=window, padding=(20, 10))
output_frame.pack(fill='x')

x_label = ttk.Label(master=output_frame, textvariable=output, padding=10, anchor='center')
x_label.pack(fill='x')

window.mainloop()