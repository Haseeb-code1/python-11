import tkinter as tk

def toggle_color():
    window.config(bg="red" if window.cget("bg") == "green" else "green")

window = tk.Tk()
window.title("Color Toggle")

button = tk.Button(window,
                  text="Click me to change color",
                  bg="green",
                  command=toggle_color)
button.pack(pady=20)

window.mainloop()