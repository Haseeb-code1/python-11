import tkinter as tk

VALID_USERNAME = "admin"
VALID_PASSWORD = "1234"

def login():
    if entry_user.get() == VALID_USERNAME and entry_pass.get() == VALID_PASSWORD:
        root.destroy()
        dashboard()
    else:
        error_label.config(text="Invalid username or password.")

def dashboard():
    win = tk.Tk()
    win.title("Dashboard")
    win.geometry("250x150")

    tk.Label(win, text="Welcome, admin!", font=("Arial", 14)).pack(pady=30)
    tk.Button(win, text="Logout", command=win.destroy).pack()

    win.mainloop()

root = tk.Tk()
root.title("Login")
root.geometry("250x180")

tk.Label(root, text="Username:").pack(pady=5)
entry_user = tk.Entry(root)
entry_user.pack()

tk.Label(root, text="Password:").pack(pady=5)
entry_pass = tk.Entry(root, show="*")
entry_pass.pack()

error_label = tk.Label(root, text="", fg="red")
error_label.pack()

tk.Button(root, text="Login", command=login).pack(pady=10)

root.mainloop()