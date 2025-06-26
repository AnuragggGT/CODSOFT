
#IMPORT NECESSARY MODULES

import tkinter as tk
from tkinter import messagebox

#define the function to perform the calculations

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operator.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                raise ZeroDivisionError #avoid the error when a number is divided by 0
            result = num1 / num2
        elif operation == '**':
            result = num1 ** num2
        elif operation == '//':
            if num2 == 0:
                raise ZeroDivisionError #avoid the error when a number is divided by 0
            result = num1 // num2
        elif operation == '%':
            if num2 == 0:
                raise ZeroDivisionError #avoid the error when a number is divided by 0
            result = num1 % num2
        else:
            messagebox.showerror("Error", "Invalid operation selected") 
            return

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers") #check if valid numbers are entered or not 
    except ZeroDivisionError:
        messagebox.showerror("Math Error", "Division by zero is not allowed") #avoid the error when a number is divided by 0

# GUI setup
root = tk.Tk()
root.title("SIMPLE CALCULATOR")
root.geometry("600x600")
root.config(bg="#DDF981")

tk.Label(root, text="ENTER FIRST NUMBER:",font=("helvetica",15), bg="#bc76ea", fg="black", width=25).grid(row=0, column=0)
entry1 = tk.Entry(root,font=("helvetica",15), bg="#a2f3d4", fg="black", width=25)
entry1.grid(row=0, column=1)

tk.Label(root, text="ENTER SECOND NUMBER:",font=("helvetica",15), bg="#bc76ea", fg="black", width=25).grid(row=1, column=0)
entry2 = tk.Entry(root,font=("helvetica",15), bg="#a2f3d4", fg="black", width=25)
entry2.grid(row=1, column=1)

tk.Label(root, text="CHOOSE:",font=("helvetica",15), bg="#0df337", fg="black", width=15).grid(row=2, column=0)

# Operation dropdown
operator = tk.StringVar()
operator.set('+')  # default value
operations = ['+', '-', '*', '/', '**', '//', '%']
tk.OptionMenu(root, operator, *operations).grid(row=2, column=1)
tk.Button(root, text="CALCULATE",font=("helvetica",15), bg="#f0874f", fg="black", width=15, command=calculate).grid(row=3, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="RESULT: ",font=("helvetica",15), bg="#81d4f2", fg="black", width=40)
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()
