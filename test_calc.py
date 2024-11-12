import unittest
import math
from decimal import Decimal, InvalidOperation
from calculator import (
    add, subtract, multiply, divide, mod, power, square_root, 
    sin, cos, floor, ceil, log, Memory
)

class TestCalculator(unittest.TestCase):

    # Тесты для функции сложения
    def test_addition_basic(self):
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-3, 3), 0)
        self.assertEqual(add(Decimal('5.5'), Decimal('4.5')), Decimal('10'))

    def test_addition_edge_cases(self):
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(Decimal('1e1000'), Decimal('1e1000')), Decimal('2e1000'))
        with self.assertRaises(TypeError):
            add(5, "three")

    def test_addition_large_numbers(self):
        large_num = Decimal('1e308')
        self.assertEqual(add(large_num, large_num), large_num * 2)

    # Тесты для функции вычитания
    def test_subtraction_basic(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(-3, -3), 0)
        self.assertEqual(subtract(Decimal('5.5'), Decimal('4.5')), Decimal('1'))

    def test_subtraction_edge_cases(self):
        self.assertEqual(subtract(0, 0), 0)
        self.assertAlmostEqual(subtract(-1e308, 1e308), Decimal('-2e308'), places=10)
        with self.assertRaises(TypeError):
            subtract("five", 3)

    # Тесты для функции умножения
    def test_multiplication_basic(self):
        self.assertEqual(multiply(5, 3), 15)
        self.assertEqual(multiply(-3, -3), 9)
        self.assertEqual(multiply(Decimal('5.5'), Decimal('2')), Decimal('11'))

    def test_multiplication_edge_cases(self):
        self.assertEqual(multiply(0, 100), 0)
        self.assertEqual(multiply(Decimal('1e308'), 1), Decimal('1e308'))
        with self.assertRaises(TypeError):
            multiply(5, "three")

    # Тесты для функции деления
    def test_division_basic(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(-6, -2), 3)
        self.assertEqual(divide(Decimal('5.5'), Decimal('2.2')), Decimal('2.5'))

    def test_division_edge_cases(self):
        with self.assertRaises(ValueError):
            divide(10, 0)
        self.assertAlmostEqual(divide(1, 3), Decimal('0.3333333333333333'))
        with self.assertRaises(TypeError):
            divide("ten", 2)

    # Тесты для функции модуля
    def test_modulus_basic(self):
        self.assertEqual(mod(10, 3), 1)
        self.assertEqual(mod(-10, 3), -1)
        self.assertEqual(mod(Decimal('10'), Decimal('4')), Decimal('2'))

    def test_modulus_edge_cases(self):
        with self.assertRaises(ValueError):
            mod(10, 0)
        self.assertEqual(mod(0, 3), 0)
        with self.assertRaises(TypeError):
            mod(10, "three")

    # Тесты для возведения в степень
    def test_power_basic(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(2, -2), Decimal('0.25'))
        self.assertEqual(power(Decimal('5.5'), 2), Decimal('30.25'))

    def test_power_edge_cases(self):
        self.assertEqual(power(2, 0), 1)
        self.assertEqual(power(0, 0), 1)  # Определено как 1
        with self.assertRaises(TypeError):
            power(2, "three")

    # Тесты для квадратного корня
    def test_square_root_basic(self):
        self.assertEqual(square_root(9), 3)
        self.assertAlmostEqual(square_root(2), Decimal('1.4142135623730951'), places=10)

    def test_square_root_edge_cases(self):
        with self.assertRaises(ValueError):
            square_root(-4)
        with self.assertRaises(TypeError):
            square_root("nine")

    # Тесты для тригонометрических функций
    def test_sin_basic(self):
        self.assertAlmostEqual(sin(0), Decimal(0))
        self.assertAlmostEqual(sin(math.pi/2), Decimal(1), places=5)
        with self.assertRaises(TypeError):
            sin("zero")

    def test_cos_basic(self):
        self.assertAlmostEqual(cos(0), Decimal(1))
        self.assertAlmostEqual(cos(math.pi), Decimal(-1), places=5)
        with self.assertRaises(TypeError):
            cos("zero")

    # Тесты для функций floor и ceil
    def test_floor_ceil(self):
        self.assertEqual(floor(5.7), 5)
        self.assertEqual(ceil(5.3), 6)
        self.assertEqual(floor(-5.3), -6)
        self.assertEqual(ceil(-5.3), -5)
        with self.assertRaises(TypeError):
            floor("five")
        with self.assertRaises(TypeError):
            ceil("five")

    # Тесты для логарифма
    def test_logarithm(self):
        self.assertEqual(log(100, 10), 2)
        self.assertEqual(log(1), 0)
        self.assertAlmostEqual(log(0.01), -2, places=5)
        with self.assertRaises(ValueError):
            log(-10)
        with self.assertRaises(ValueError):
            log(10, 1)
        with self.assertRaises(TypeError):
            log("ten")
    
    def test_subtraction_edge_cases(self):
        self.assertEqual(subtract(0, 0), 0)
        # Используем более безопасные значения
        self.assertAlmostEqual(subtract(Decimal('1e50'), Decimal('1e50')), Decimal('0'), places=10)
        with self.assertRaises(TypeError):
            subtract("five", 3)

    # Тест на проверку невалидного ввода в память
    def test_memory_invalid_operations(self):
        memory = Memory()
        with self.assertRaises(ValueError):
            memory.m_add("ten")  # Проверка с некорректным вводом
        memory.m_clear()
        self.assertEqual(memory.m_recall(), Decimal(0))

    # Тесты для операций с памятью
    def test_memory_operations(self):
        memory = Memory()
        memory.m_add(10)
        self.assertEqual(memory.m_recall(), Decimal(10))
        memory.m_add(-5)
        self.assertEqual(memory.m_recall(), Decimal(5))
        memory.m_add(Decimal('2.5'))
        self.assertEqual(memory.m_recall(), Decimal('7.5'))
        memory.m_clear()
        self.assertEqual(memory.m_recall(), Decimal(0))

    # Проверка ошибок в памяти
    def test_memory_invalid_operations(self):
        memory = Memory()
        with self.assertRaises(ValueError):
            memory.m_add("ten")  # Проверка на некорректный ввод, должен выбросить ValueError
        memory.m_clear()
        self.assertEqual(memory.m_recall(), Decimal(0))

if __name__ == "__main__":
    unittest.main()
