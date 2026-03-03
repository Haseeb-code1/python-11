import tkinter as tk

def handle_click(event):
    print(f"Button clicked at X={event.x}, Y={event.y}")

def handle_key(event):
    print(f"Key pressed: {event.char}")

window = tk.Tk()
button = tk.Button(window, text="Click Me")
button.pack()

entry = tk.Entry(window)
entry.pack()


button.bind("<Button-1>", handle_click)


entry.bind("<Key>", handle_key)

window.mainloop()