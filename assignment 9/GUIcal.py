import tkinter as tk
from tkinter import messagebox

def press_button(value):
    current_text = entry_box.get()
    entry_box.delete(0, tk.END)
    entry_box.insert(0, current_text + str(value))

def calculate_result():
    try:
        expression = entry_box.get()
        result = eval(expression)  # Evaluate the expression
        entry_box.delete(0, tk.END)
        entry_box.insert(0, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid Expression")

def clear_entry():
    entry_box.delete(0, tk.END)

root = tk.Tk()
root.title("Calculator")

root.geometry("300x400")

entry_box = tk.Entry(root, font=("Arial", 20), borderwidth=2, relief="solid", justify="right")
entry_box.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0), ('%', 5, 1)  
]

for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, font=("Arial", 18), command=calculate_result)
    elif text == 'C':
        button = tk.Button(root, text=text, font=("Arial", 18), command=clear_entry)
    else:
        button = tk.Button(root, text=text, font=("Arial", 18), command=lambda value=text: press_button(value))
    
    button.grid(row=row, column=col, sticky="nsew", ipadx=10, ipady=10)


for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

root.mainloop()
