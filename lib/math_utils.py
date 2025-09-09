import math

def square(n):
    """
    Returns the square of a number n.
    """
    if not isinstance(n, (int, float)):
        raise TypeError("The argument must be a number (int or float).")
    return n ** 2

def factorial(n):
    """
    Returns the factorial of a non-negative integer n.
    """
    if not isinstance(n, int):
        raise TypeError("Factorial is only defined for integers.")
    if n < 0:
        raise ValueError("Factorial is only defined for non-negative integers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def is_prime(n):
    """
    Returns True if n is a prime number, False otherwise.
    """
    if not isinstance(n, int):
        raise TypeError("The argument must be an integer.")
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def gcd(a, b):
    """
    Returns the greatest common divisor (GCD) of two integers a and b.
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both arguments must be integers.")
    while b != 0:
        a, b = b, a % b
    return abs(a)

def lcm(a, b):
    """
    Returns the least common multiple (LCM) of two integers a and b.
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both arguments must be integers.")
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)