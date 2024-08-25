import ttkbootstrap as ttk
from tkinter import messagebox
import sympy as sy


def calculate():
    try:
        l, r = equ.get().strip().split('=')
        output.set('')
        eqx = sy.Eq(sy.sympify(l), sy.sympify(r))
        solved = sy.solve(eqx)
        output.set(solved)
    except:
        messagebox.showerror('Invalid input', 'You need to enter a valid equation!')

def clear():
    equ_entry.delete(0, ttk.END)
    equ_entry.focus()


# Set up the main window
window = ttk.Window(themename='superhero')
window.title("Find Your X")
window.geometry('400x250')
window.resizable(False, False)

# Variables
equ = ttk.StringVar()
output = ttk.StringVar()  # Changed to StringVar for better display of solutions

# Input Frame
input_frame = ttk.Frame(master=window, padding=(20, 10))
input_frame.pack(fill='x')

label = ttk.Label(master=input_frame, text='Enter your Equation:', anchor='w')
label.pack(fill='x')

equ_entry = ttk.Entry(master=input_frame, textvariable=equ, justify='center')
equ_entry.pack(fill='x', pady=5)
equ_entry.focus()

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
