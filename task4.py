import tkinter as tk
window = tk.Tk()

label = tk.Label(window, text="Hello, Tkinter", fg="blue", bg="yellow", padx=10,
pady=5)
label.pack()

button = tk.Button(window, text="Click Me", width=15, command=lambda:
print("Button clicked"))
button.pack()

window.mainloop()