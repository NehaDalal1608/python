import tkinter as tk
from tkinter import messagebox
import re

def submit_form():

    username = entry_username.get()
    password = entry_password.get()
    email = entry_email.get()

    if not username.isalpha():
        messagebox.showerror("Invalid Username", "Username should only contain alphabets.")
        return

    if not password.isdigit():
        messagebox.showerror("Invalid Password", "Password should only contain numbers.")
        return

    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if not re.match(email_pattern, email):
        messagebox.showerror("Invalid Email", "Please enter a valid email address.")
        return

    messagebox.showinfo("Registration Successful", f"Welcome, {username}!\nYour email: {email}")

root = tk.Tk()
root.title("Registration Form")


root.geometry("300x250")

label_username = tk.Label(root, text="Username")
label_username.pack()
entry_username = tk.Entry(root)
entry_username.pack()

label_password = tk.Label(root, text="Password")
label_password.pack()
entry_password = tk.Entry(root, show="*")  # Hide password input
entry_password.pack()

label_email = tk.Label(root, text="Email")
label_email.pack()
entry_email = tk.Entry(root)
entry_email.pack()

submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.pack()

root.mainloop()
