import tkinter as tk
from tkinter import messagebox

def calculate_selling_price():
    try:
        total_cost = float(total_cost_entry.get())
        quantity = float(quantity_entry.get())
        profit_percent = float(profit_entry.get())

        cost_per_item = total_cost / quantity
        selling_price = cost_per_item * (1 + profit_percent / 100)

        selling_price_entry.delete(0, tk.END)
        selling_price_entry.insert(0, f"{selling_price:.2f}")

        result_label.config(
            text=f"Sell each item at: {selling_price:.2f}"
        )

    except ValueError:
        messagebox.showerror("Error", "Enter valid numbers for Cost, Quantity, and Profit %")

def calculate_profit():
    try:
        total_cost = float(total_cost_entry.get())
        quantity = float(quantity_entry.get())
        selling_price = float(selling_price_entry.get())

        cost_per_item = total_cost / quantity
        profit_percent = ((selling_price / cost_per_item) - 1) * 100

        profit_entry.delete(0, tk.END)
        profit_entry.insert(0, f"{profit_percent:.2f}")

        result_label.config(
            text=f"Your profit margin is: {profit_percent:.2f}%"
        )

    except ValueError:
        messagebox.showerror("Error", "Enter valid numbers for Cost, Quantity, and Selling Price")

# Window
root = tk.Tk()
root.title("Item Price & Profit Calculator")
root.geometry("400x400")

tk.Label(root, text="Total Cost").pack()
total_cost_entry = tk.Entry(root)
total_cost_entry.pack()

tk.Label(root, text="Quantity (number of items)").pack()
quantity_entry = tk.Entry(root)
quantity_entry.pack()

tk.Label(root, text="Profit %").pack()
profit_entry = tk.Entry(root)
profit_entry.pack()

tk.Label(root, text="Selling Price per Item").pack()
selling_price_entry = tk.Entry(root)
selling_price_entry.pack()

button_frame = tk.Frame(root)
button_frame.pack(pady=15)

tk.Button(button_frame, text="Calculate Selling Price", command=calculate_selling_price).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Calculate Profit %", command=calculate_profit).pack(side=tk.LEFT, padx=5)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=20)

root.mainloop()