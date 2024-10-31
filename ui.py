import tkinter as tk
from main import add, subtract, multiply, divide, mod, power, square_root, sin, cos, floor, ceil, Memory

# Инициализация интерфейса
root = tk.Tk()
root.title("Calculator")

# Объект памяти для работы с m+ и mc
memory = Memory()

# Поля для ввода и вывода
entry1 = tk.Entry(root)
entry1.grid(row=0, column=0, columnspan=4)

entry2 = tk.Entry(root)
entry2.grid(row=1, column=0, columnspan=4)

result_label = tk.Label(root, text="Result: ")
result_label.grid(row=2, column=0, columnspan=4)

# Функции для кнопок
def on_add():
    result = add(float(entry1.get()), float(entry2.get()))
    result_label.config(text="Result: " + str(result))

def on_subtract():
    result = subtract(float(entry1.get()), float(entry2.get()))
    result_label.config(text="Result: " + str(result))

def on_multiply():
    result = multiply(float(entry1.get()), float(entry2.get()))
    result_label.config(text="Result: " + str(result))

def on_divide():
    try:
        result = divide(float(entry1.get()), float(entry2.get()))
        result_label.config(text="Result: " + str(result))
    except ValueError as e:
        result_label.config(text="Error: " + str(e))

def on_mod():
    result = mod(float(entry1.get()), float(entry2.get()))
    result_label.config(text="Result: " + str(result))

def on_power():
    result = power(float(entry1.get()), float(entry2.get()))
    result_label.config(text="Result: " + str(result))

def on_square_root():
    try:
        result = square_root(float(entry1.get()))
        result_label.config(text="Result: " + str(result))
    except ValueError as e:
        result_label.config(text="Error: " + str(e))

def on_sin():
    result = sin(float(entry1.get()))
    result_label.config(text="Result: " + str(result))

def on_cos():
    result = cos(float(entry1.get()))
    result_label.config(text="Result: " + str(result))

def on_floor():
    result = floor(float(entry1.get()))
    result_label.config(text="Result: " + str(result))

def on_ceil():
    result = ceil(float(entry1.get()))
    result_label.config(text="Result: " + str(result))

# Функции для работы с памятью
def on_memory_add():
    memory.m_add(float(entry1.get()))
    result_label.config(text="Memory: " + str(memory.m_recall()))

def on_memory_clear():
    memory.m_clear()
    result_label.config(text="Memory cleared")

def on_memory_recall():
    result_label.config(text="Memory: " + str(memory.m_recall()))

# Кнопки для каждой функции
tk.Button(root, text="+", command=on_add).grid(row=3, column=0)
tk.Button(root, text="-", command=on_subtract).grid(row=3, column=1)
tk.Button(root, text="*", command=on_multiply).grid(row=3, column=2)
tk.Button(root, text="/", command=on_divide).grid(row=3, column=3)
tk.Button(root, text="mod", command=on_mod).grid(row=4, column=0)
tk.Button(root, text="pow", command=on_power).grid(row=4, column=1)
tk.Button(root, text="√", command=on_square_root).grid(row=4, column=2)
tk.Button(root, text="sin", command=on_sin).grid(row=4, column=3)
tk.Button(root, text="cos", command=on_cos).grid(row=5, column=0)
tk.Button(root, text="floor", command=on_floor).grid(row=5, column=1)
tk.Button(root, text="ceil", command=on_ceil).grid(row=5, column=2)

# Кнопки для операций с памятью
tk.Button(root, text="M+", command=on_memory_add).grid(row=6, column=0)
tk.Button(root, text="MC", command=on_memory_clear).grid(row=6, column=1)
tk.Button(root, text="MR", command=on_memory_recall).grid(row=6, column=2)

# Запуск основного цикла интерфейса
root.mainloop()

