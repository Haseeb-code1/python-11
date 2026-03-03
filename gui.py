import tkinter as tk
from contextlib import nullcontext

from pyexpat.errors import messages


def login_buttonclick():
    print("login button")
    input_user = user_name.get()
    input_password = user_password.get()
    print("user name: ", input_user)
    print("user password: ", input_password)
    if input_user=="haseeb" and input_password=="123":
        message_lable.config(text="login successful")
    else:
        message_lable.config(text="login failed")






window = tk.Tk()
window.title("my window")
window.geometry("500x500")
user_lable = tk.Label(window, text=" loginpage !", font=("Arial", 25), fg="white", bg="blue")

user_lable.pack()


user_namelable = tk.Label(window, text=" user name!", font=("Arial", 14), fg="white", bg="black")

user_namelable.pack()
user_name = tk.Entry(window, font=("Arial", 18), fg="black", bg="white")
user_name.pack()

user_lablepassword = tk.Label(window, text=" password", font=("Arial", 14), fg="white", bg="black")

user_lablepassword.pack()

user_password = tk.Entry(window, font=("Arial", 18), fg="black", bg="white")
user_password.pack()

login_button = tk.Button(window, text="login", font=("Arial", 18), command=login_buttonclick)
login_button.pack()
message_lable=tk.Label(window, text="", font=("Arial", 14), fg="black")
message_lable.pack()
window.mainloop()
message_lable.pack()
window.mainloop()
