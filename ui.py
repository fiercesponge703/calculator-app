import tkinter as tk
from calculator import add, subtract, multiply, divide, mod, power, square_root, sin, cos, floor, ceil, Memory

def get_number(entry):
    try:
        return float(entry.get())
    except ValueError:
        raise ValueError("Invalid input. Please enter a numeric value.")


root = tk.Tk()
root.title("Calculator")


entry1 = tk.Entry(root)
entry1.grid(row=0, column=0, columnspan=2)

entry2 = tk.Entry(root)
entry2.grid(row=1, column=0, columnspan=2)

result_label = tk.Label(root, text="Result:")
result_label.grid(row=2, column=0, columnspan=2)


# Функции для каждой операции с обработкой ошибок
def on_add():
    try:
        num1 = get_number(entry1)
        num2 = get_number(entry2)
        result = add(num1, num2)
        result_label.config(text="Result: " + str(result))
    except ValueError as e:
        result_label.config(text="Error: " + str(e))

def on_subtract():
    try:
        num1 = get_number(entry1)
        num2 = get_number(entry2)
        result = subtract(num1, num2)
        result_label.config(text="Result: " + str(result))
    except ValueError as e:
        result_label.config(text="Error: " + str(e))

def on_multiply():
    try:
        num1 = get_number(entry1)
        num2 = get_number(entry2)
        result = multiply(num1, num2)
        result_label.config(text="Result: " + str(result))
    except ValueError as e:
        result_label.config(text="Error: " + str(e))

def on_divide():
    try:
        num1 = get_number(entry1)
        num2 = get_number(entry2)
        result = divide(num1, num2)
        result_label.config(text="Result: " + str(result))
    except ValueError as e:
        result_label.config(text="Error: " + str(e))
    except ZeroDivisionError:
        result_label.config(text="Error: Division by zero is not allowed.")

def on_mod():
    try:
        num1 = get_number(entry1)
        num2 = get_number(entry2)
        result = mod(num1, num2)
        result_label.config(text="Result: " + str(result))
    except ValueError as e:
        result_label.config(text="Error: " + str(e))
    except ZeroDivisionError:
        result_label.config(text="Error: Modulus by zero is not allowed.")

def on_power():
    try:
        num1 = get_number(entry1)
        num2 = get_number(entry2)
        result = power(num1, num2)
        result_label.config(text="Result: " + str(result))
    except ValueError as e:
        result_label.config(text="Error: " + str(e))

def on_square_root():
    try:
        num1 = get_number(entry1)
        result = square_root(num1)
        result_label.config(text="Result: " + str(result))
    except ValueError:
        result_label.config(text="Error: Cannot compute square root of a negative number.")

def on_sin():
    try:
        num1 = get_number(entry1)
        result = sin(num1)
        result_label.config(text="Result: " + str(result))
    except ValueError as e:
        result_label.config(text="Error: " + str(e))

def on_cos():
    try:
        num1 = get_number(entry1)
        result = cos(num1)
        result_label.config(text="Result: " + str(result))
    except ValueError as e:
        result_label.config(text="Error: " + str(e))

def on_floor():
    try:
        num1 = get_number(entry1)
        result = floor(num1)
        result_label.config(text="Result: " + str(result))
    except ValueError as e:
        result_label.config(text="Error: " + str(e))

def on_ceil():
    try:
        num1 = get_number(entry1)
        result = ceil(num1)
        result_label.config(text="Result: " + str(result))
    except ValueError as e:
        result_label.config(text="Error: " + str(e))

# Кнопки для операций
tk.Button(root, text="Add", command=on_add).grid(row=3, column=0)
tk.Button(root, text="Subtract", command=on_subtract).grid(row=3, column=1)
tk.Button(root, text="Multiply", command=on_multiply).grid(row=4, column=0)
tk.Button(root, text="Divide", command=on_divide).grid(row=4, column=1)
tk.Button(root, text="Modulus", command=on_mod).grid(row=5, column=0)
tk.Button(root, text="Power", command=on_power).grid(row=5, column=1)
tk.Button(root, text="Square Root", command=on_square_root).grid(row=6, column=0)
tk.Button(root, text="Sin", command=on_sin).grid(row=6, column=1)
tk.Button(root, text="Cos", command=on_cos).grid(row=7, column=0)
tk.Button(root, text="Floor", command=on_floor).grid(row=7, column=1)
tk.Button(root, text="Ceil", command=on_ceil).grid(row=8, column=0)

def get_number(entry):
    try:
        return float(entry.get())
    except ValueError:
        raise ValueError("Invalid input. Please enter a numeric value.")

memory = Memory()

def on_memory_add():
    try:
        value = get_number(entry1)
        memory.m_add(value)
        result_label.config(text="Memory updated: " + str(memory.m_recall()))
    except ValueError as e:
        result_label.config(text="Error: " + str(e))

def on_memory_subtract():
    try:
        value = get_number(entry1)
        memory.m_subtract(value)
        result_label.config(text="Memory updated: " + str(memory.m_recall()))
    except ValueError as e:
        result_label.config(text="Error: " + str(e))

def on_memory_multiply():
    try:
        value = get_number(entry1)
        memory.m_multiply(value)
        result_label.config(text="Memory updated: " + str(memory.m_recall()))
    except ValueError as e:
        result_label.config(text="Error: " + str(e))

def on_memory_divide():
    try:
        value = get_number(entry1)
        memory.m_divide(value)
        result_label.config(text="Memory updated: " + str(memory.m_recall()))
    except ValueError as e:
        result_label.config(text="Error: " + str(e))

def on_memory_clear():
    memory.m_clear()
    result_label.config(text="Memory cleared")

def on_memory_recall():
    result_label.config(text="Memory: " + str(memory.m_recall()))

def on_memory_history():
    history = memory.get_history()
    result_label.config(text="Memory History: " + str(history))

def on_memory_delete_last():
    try:
        memory.delete_last()
        result_label.config(text="Last item removed. Memory: " + str(memory.m_recall()))
    except ValueError as e:
        result_label.config(text="Error: " + str(e))

# Кнопки для работы с памятью
tk.Button(root, text="M+", command=on_memory_add).grid(row=9, column=0)
tk.Button(root, text="M-", command=on_memory_subtract).grid(row=9, column=1)
tk.Button(root, text="M*", command=on_memory_multiply).grid(row=10, column=0)
tk.Button(root, text="M/", command=on_memory_divide).grid(row=10, column=1)
tk.Button(root, text="MC", command=on_memory_clear).grid(row=11, column=0)
tk.Button(root, text="MR", command=on_memory_recall).grid(row=11, column=1)
tk.Button(root, text="History", command=on_memory_history).grid(row=12, column=0)
tk.Button(root, text="Delete Last", command=on_memory_delete_last).grid(row=12, column=1)

root.mainloop()

