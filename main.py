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
def power(base, exponent):
    return base ** exponent
import math

def square_root(x):
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number")
    return math.sqrt(x)
def floor(x):
    return math.floor(x)
def ceil(x):
    return math.ceil(x)

class Memory:
    def __init__(self):
        self.memory = 0

    def m_add(self, value):
        self.memory += value

    def m_clear(self):
        self.memory = 0

    def m_recall(self):
        return self.memory
