
import unittest

from calculator import (
    add, subtract, multiply,
    divide, modulus, power
)


class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(add(10, 5), 15)

    def test_subtraction(self):
        self.assertEqual(subtract(10, 5), 5)

    def test_multiplication(self):
        self.assertEqual(multiply(10, 5), 50)

    def test_division(self):
        self.assertEqual(divide(10, 5), 2)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_modulus(self):
        self.assertEqual(modulus(10, 3), 1)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)

    def test_negative_numbers(self):
        self.assertEqual(add(-5, 3), -2)


if __name__ == "__main__":
    unittest.main()
