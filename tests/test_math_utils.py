import unittest
from math_utils.core import *


class TestMathFunctions(unittest.TestCase):

    # ========== Tests for square ==========
    def test_square_positive(self):
        self.assertEqual(square(5), 25)

    def test_square_negative(self):
        self.assertEqual(square(-3), 9)

    def test_square_float(self):
        self.assertAlmostEqual(square(2.5), 6.25)

    def test_square_invalid(self):
        with self.assertRaises(TypeError):
            square("a")

    # ========== Tests for factorial ==========
    def test_factorial_basic(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)

    def test_factorial_invalid_type(self):
        with self.assertRaises(TypeError):
            factorial(3.5)

    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            factorial(-2)

    # ========== Tests for is_prime ==========
    def test_is_prime_true(self):
        for n in [2, 3, 13, 17]:
            self.assertTrue(is_prime(n))

    def test_is_prime_false(self):
        for n in [0, 1, 9, -7]:
            self.assertFalse(is_prime(n))

    def test_is_prime_invalid_type(self):
        with self.assertRaises(TypeError):
            is_prime(3.5)

    # ========== Tests for gcd ==========
    def test_gcd_positive(self):
        self.assertEqual(gcd(12, 18), 6)
        self.assertEqual(gcd(18, 12), 6)

    def test_gcd_negative(self):
        self.assertEqual(gcd(-12, 18), 6)
        self.assertEqual(gcd(-12, -18), 6)

    def test_gcd_with_zero(self):
        self.assertEqual(gcd(0, 5), 5)
        self.assertEqual(gcd(5, 0), 5)
        self.assertEqual(gcd(0, 0), 0)

    def test_gcd_invalid_type(self):
        with self.assertRaises(TypeError):
            gcd(12, 3.5)

    # ========== Tests for lcm ==========
    def test_lcm_positive(self):
        self.assertEqual(lcm(12, 18), 36)
        self.assertEqual(lcm(18, 12), 36)

    def test_lcm_negative(self):
        self.assertEqual(lcm(-12, 18), 36)
        self.assertEqual(lcm(-12, -18), 36)

    def test_lcm_with_zero(self):
        self.assertEqual(lcm(0, 5), 0)
        self.assertEqual(lcm(5, 0), 0)
        self.assertEqual(lcm(0, 0), 0)

    def test_lcm_invalid_type(self):
        with self.assertRaises(TypeError):
            lcm(12, 3.5)


if __name__ == "__main__":
    unittest.main()
