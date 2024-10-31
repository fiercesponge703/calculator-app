import math

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

# main.py
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def mod(a, b):
    return a % b
