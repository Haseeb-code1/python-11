import tkinter as tk

def celsius_to_fahrenheit():
    try:
        celsius = float(entry_celsius.get())
        fahrenheit = (celsius * 9/5) + 32
        output_label.config(text=f"{fahrenheit:.2f} °F", fg="blue")
    except ValueError:
        output_label.config(text="Invalid Input! Enter a number.", fg="red")

def fahrenheit_to_celsius():
    try:
        fahrenheit = float(entry_fahrenheit.get())
        celsius = (fahrenheit - 32) * 5/9
        output_label2.config(text=f"{celsius:.2f} °C", fg="green")
    except ValueError:
        output_label2.config(text="Invalid Input! Enter a number.", fg="red")

window = tk.Tk()
window.title("Temperature Converter")
window.geometry("400x400")
window.configure(bg="#f0f0f0")

title_label = tk.Label(window, text="Temperature Converter", font=("Arial", 16, "bold"), bg="#f0f0f0")
title_label.pack(pady=(10, 0))

section1 = tk.Label(window, text="Celsius to Fahrenheit", font=("Arial", 11, "bold"), bg="#f0f0f0", fg="#333")
section1.pack(pady=(10, 2))

row1 = tk.Frame(window, bg="#f0f0f0")
row1.pack()

label_celsius = tk.Label(row1, text="Celsius:", bg="#f0f0f0", font=("Arial", 10))
label_celsius.pack( padx=10)

entry_celsius = tk.Entry(row1, width=15, font=("Arial", 10))
entry_celsius.pack( padx=5)

convert_btn1 = tk.Button(row1, text="Convert →", command=celsius_to_fahrenheit,
                          bg="#4CAF50", fg="white", font=("Arial", 10), relief="flat", padx=8)
convert_btn1.pack( padx=5)

output_label = tk.Label(window, text="Result will appear here", font=("Arial", 11), bg="#f0f0f0", fg="blue")
output_label.pack(pady=5)

sep = tk.Frame(window, height=2, bg="#cccccc")
sep.pack(padx=20, pady=10)

section2 = tk.Label(window, text="Fahrenheit to Celsius", font=("Arial", 11, "bold"), bg="#f0f0f0", fg="#333")
section2.pack(pady=(2, 2))

row2 = tk.Frame(window, bg="#f0f0f0")
row2.pack()

label_fahrenheit = tk.Label(row2, text="Fahrenheit:", bg="#f0f0f0", font=("Arial", 10))
label_fahrenheit.pack(padx=10)

entry_fahrenheit = tk.Entry(row2, width=15, font=("Arial", 10))
entry_fahrenheit.pack( padx=5)

convert_btn2 = tk.Button(row2, text="Convert →", command=fahrenheit_to_celsius,
                          bg="#2196F3", fg="white", font=("Arial", 10), relief="flat", padx=8)
convert_btn2.pack( padx=5)

output_label2 = tk.Label(window, text="Result will appear here", font=("Arial", 11), bg="#f0f0f0", fg="green")
output_label2.pack(pady=5)

window.mainloop()