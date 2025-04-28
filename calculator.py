import tkinter as tk
from tkinter import messagebox

def add():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        ans = num1 + num2
        label_result.config(text="Result: " + str(ans))
    except:
        messagebox.showerror("Error", "Invalid Input")

def subtract():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        ans = num1 - num2
        label_result.config(text="Result: " + str(ans))
    except:
        messagebox.showerror("Error", "Invalid Input")

def multiply():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        ans = num1 * num2
        label_result.config(text="Result: " + str(ans))
    except:
        messagebox.showerror("Error", "Invalid Input")

def divide():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if num2 == 0:
            messagebox.showerror("Error", "Cannot divide by 0")
        else:
            ans = num1 / num2
            label_result.config(text="Result: " + str(ans))
    except:
        messagebox.showerror("Error", "Invalid Input")

# window setup
root = tk.Tk()
root.title("Calculator")
root.geometry("300x300")

entry1 = tk.Entry(root)
entry1.pack(pady=10)

entry2 = tk.Entry(root)
entry2.pack(pady=10)

btn_add = tk.Button(root, text="Add", command=add)
btn_add.pack(pady=5)

btn_subtract = tk.Button(root, text="Subtract", command=subtract)
btn_subtract.pack(pady=5)

btn_multiply = tk.Button(root, text="Multiply", command=multiply)
btn_multiply.pack(pady=5)

btn_divide = tk.Button(root, text="Divide", command=divide)
btn_divide.pack(pady=5)

label_result = tk.Label(root, text="Result: ")
label_result.pack(pady=20)

root.mainloop()
