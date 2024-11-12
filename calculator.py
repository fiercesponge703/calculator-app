import math
from decimal import Decimal, InvalidOperation

def validate_number(value):
    """Проверка, что значение является числом."""
    if not isinstance(value, (int, float, Decimal)):
        raise TypeError("Argument must be a number")
    return Decimal(value)

def add(a, b):
    a, b = validate_number(a), validate_number(b)
    return a + b

def subtract(a, b):
    a, b = validate_number(a), validate_number(b)
    return a - b

def multiply(a, b):
    a, b = validate_number(a), validate_number(b)
    return a * b

def divide(a, b):
    a, b = validate_number(a), validate_number(b)
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def mod(a, b):
    a, b = validate_number(a), validate_number(b)
    if b == 0:
        raise ValueError("Cannot calculate modulus with zero")
    return a % b

def power(base, exponent):
    base, exponent = validate_number(base), validate_number(exponent)
    if base == 0 and exponent == 0:
        return Decimal(1)  # Определяем 0 ** 0 как 1
    return base ** exponent


def square_root(x):
    x = validate_number(x)
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number")
    return x.sqrt()

def sin(x):
    x = validate_number(x)
    return Decimal(math.sin(float(x)))

def cos(x):
    x = validate_number(x)
    return Decimal(math.cos(float(x)))

def floor(x):
    x = validate_number(x)
    return math.floor(x)

def ceil(x):
    x = validate_number(x)
    return math.ceil(x)

def log(x, base=10):
    x, base = validate_number(x), validate_number(base)
    if x <= 0:
        raise ValueError("Logarithm undefined for non-positive values")
    if base <= 0 or base == 1:
        raise ValueError("Base of logarithm must be positive and not equal to 1")
    return x.log10() / base.log10()

from decimal import Decimal, InvalidOperation

def validate_decimal(value):
    """Проверяет, что значение может быть преобразовано в Decimal."""
    try:
        return Decimal(value)
    except (InvalidOperation, ValueError):
        raise ValueError("Invalid input: value must be a number")

class Memory:
    def __init__(self):
        self.memory = Decimal(0)
        self.history = []

    def m_add(self, value):
        value = validate_decimal(value)  # Валидация значения
        self.memory += value
        self.history.append(value)

    def m_subtract(self, value):
        value = validate_decimal(value)
        self.memory -= value
        self.history.append(-value)

    def m_multiply(self, value):
        value = validate_decimal(value)
        self.memory *= value
        self.history.append(f"*{value}")

    def m_divide(self, value):
        value = validate_decimal(value)
        if value == 0:
            raise ValueError("Cannot divide by zero in memory")
        self.memory /= value
        self.history.append(f"/{value}")

    def m_clear(self):
        self.memory = Decimal(0)
        self.history.clear()

    def m_recall(self):
        return self.memory

    def get_history(self):
        return self.history

    def delete_last(self):
        if self.history:
            last_value = self.history.pop()
            if isinstance(last_value, Decimal):
                self.memory -= last_value
            elif isinstance(last_value, str):
                operator = last_value[0]
                value = Decimal(last_value[1:])
                if operator == "*":
                    self.memory /= value
                elif operator == "/":
                    self.memory *= value
        else:
            raise ValueError("No items in memory to delete")
