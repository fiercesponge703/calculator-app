import unittest
from main import add, subtract, multiply, divide, mod, power, square_root, sin, cos, floor, ceil, Memory

class TestCalculator(unittest.TestCase):

    # Тесты для основных арифметических операций
    def test_addition(self):
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtraction(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(-1, -1), 0)
        self.assertEqual(subtract(0, 5), -5)

    def test_multiplication(self):
        self.assertEqual(multiply(5, 3), 15)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(0, 5), 0)

    def test_division(self):
        self.assertEqual(divide(10, 2), 5)
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_modulus(self):
        self.assertEqual(mod(10, 3), 1)
        self.assertEqual(mod(10, 5), 0)

    # Тесты для тригонометрических функций
    def test_sin(self):
        self.assertAlmostEqual(sin(0), 0)
        self.assertAlmostEqual(sin(3.14159 / 2), 1, places=4)  # π/2 ≈ 1.5708

    def test_cos(self):
        self.assertAlmostEqual(cos(0), 1)
        self.assertAlmostEqual(cos(3.14159), -1, places=4)  # π ≈ 3.14159

    # Тесты для функций возведения в степень и квадратного корня
    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)

    def test_square_root(self):
        self.assertEqual(square_root(9), 3)
        with self.assertRaises(ValueError):
            square_root(-4)

    # Тесты для округления
    def test_floor(self):
        self.assertEqual(floor(5.7), 5)
        self.assertEqual(floor(-2.3), -3)

    def test_ceil(self):
        self.assertEqual(ceil(5.3), 6)
        self.assertEqual(ceil(-2.7), -2)

    # Тесты для операций с памятью
    def test_memory_operations(self):
        memory = Memory()
        memory.m_add(10)
        self.assertEqual(memory.m_recall(), 10)
        memory.m_add(5)
        self.assertEqual(memory.m_recall(), 15)
        memory.m_clear()
        self.assertEqual(memory.m_recall(), 0)

if __name__ == "__main__":
    unittest.main()
