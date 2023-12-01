"""
    My mathematical functions
"""


from complex import Complex


def Re(z: Complex | float | int) -> float:
    if not isinstance(z, Complex):
        return z
    return z.real


def Im(z: Complex | int | float) -> float:
    if not isinstance(z, Complex):
        return z
    return z.imaginary


def ft_abs(number: int | float | Complex, method='euclid') -> int | float:
    """ Returns absolute value of number """
    if isinstance(number, (int, float)):
        return number if number >= 0 else -number
    elif isinstance(number, Complex):
        if method == 'euclid':
            return ft_sqrt(number.real * number.real + number.imaginary * number.imaginary)
        elif method == 'manhattan':
            return ft_abs(number.real) + ft_abs(number.imaginary)
    else:
        raise AssertionError("Value must be a number.")


def ft_pow(x: float | int, n: int) -> float:
    """ Returns value x^n, recursive way """
    if not isinstance(x, (float, int)) or not isinstance(n, int):
        raise AssertionError("Values must be float for x, and int for n.")
    if n < 0:
        raise AssertionError("Cannot calculate for a negative power.")
    elif n == 0:
        return 1
    else:
        return x * ft_pow(x, n - 1)


def ft_sqrt(number: int | float, epsilon=1e-14, max_iterations=2000) -> int | float:
    """ Returns an approximation of square root, using Newton-Raphson method. """
    if not isinstance(number, (int, float)) or number < 0:
        raise AssertionError("Value must be a positive number.")
    if number == 0:
        return 0.0

    x = 1.

    for _ in range(max_iterations):
        x = (x + number / x) / 2

        if (x * x - number) < epsilon:
            return x

    raise AssertionError("Method didn't converge enough.")
