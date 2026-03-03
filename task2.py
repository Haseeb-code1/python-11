import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = entry_name.get()
    email = entry_email.get()
    phone = entry_phone.get()
    result_label.config(text=f"Name: {name}\nEmail: {email}\nPhone: {phone if phone else 'N/A'}", fg="green")



window = tk.Tk()
window.title("User Registration Form")
window.geometry("350x280")

title = tk.Label(window, text="User Registration Form", font=("Arial", 14, "bold"))
title.grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(window, text="Name:", font=("Arial", 11)).grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_name = tk.Entry(window, width=25)
entry_name.grid(row=1, column=1, pady=5)

tk.Label(window, text="Email:", font=("Arial", 11)).grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_email = tk.Entry(window, width=25)
entry_email.grid(row=2, column=1, pady=5)

tk.Label(window, text="Phone:", font=("Arial", 11)).grid(row=3, column=0, padx=10, pady=5, sticky="e")
entry_phone = tk.Entry(window, width=25)
entry_phone.grid(row=3, column=1, pady=5)

tk.Button(window, text="Submit", command=submit_form, width=10).grid(row=4, column=0, pady=10)


result_label = tk.Label(window, text="", font=("Arial", 10))
result_label.grid(row=5, column=0, columnspan=2, pady=5)

window.mainloop()