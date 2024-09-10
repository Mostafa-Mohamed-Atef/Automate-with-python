import tkinter as tk
from tkinter import ttk
import requests
import json

def get_currency():
    with open("key.json", "r") as file:
        data = json.load(file)
        api_key = data["api_key"]
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"
    response = requests.get(url)
    data = response.json()
    return data["conversion_rates"]["EGP"]

def convert_currency():
    try:
        usd_amount = float(usd_entry.get())
        egp_rate = get_currency()
        egp_amount = usd_amount * egp_rate
        result_label.config(text=f"{usd_amount:,.2f} USD = {egp_amount:,.2f} EGP")
    except ValueError:
        result_label.config(text="Please enter a valid number")

# Create the main window
root = tk.Tk()
root.title("EGP2USD")
root.geometry("350x250")
root.configure(bg="#1E1E1E")

# Configure styles
style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", foreground="#FFFFFF", background="#1E1E1E", font=("Arial", 12))
style.configure("TEntry", fieldbackground="#2E2E2E", foreground="#FFFFFF", font=("Arial", 12))
style.configure("TButton", background="#3E3E3E", foreground="#FFFFFF", font=("Arial", 12))
style.map("TButton", background=[("active", "#4E4E4E")])

# Create and place widgets
title_label = ttk.Label(root, text=f"The Exchange Rate is {get_currency()}", font=("Arial", 18, "bold"))
title_label.pack(pady=20)

usd_frame = ttk.Frame(root, style="TLabel")
usd_frame.pack(pady=10)

usd_label = ttk.Label(usd_frame, text="USD:")
usd_label.pack(side="left", padx=5)

usd_entry = ttk.Entry(usd_frame, width=15)
usd_entry.pack(side="left")

convert_button = ttk.Button(root, text="Convert", command=convert_currency)
convert_button.pack(pady=15)

result_label = ttk.Label(root, text="", font=("Arial", 14))
result_label.pack()

# Start the GUI event loop
root.mainloop()
