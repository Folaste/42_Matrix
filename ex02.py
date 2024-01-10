"""
    Exercise 02: Linear Interpolation
"""


from complex import Complex
from matrix import Matrix
from vector import Vector


def lerp(u, v, t) -> int | float | Complex | Matrix | Vector:
    """ Returns linear interpolation between u and v with factor t. """
    # Time complexity: O(1)
    # Space complexity: O(1)
    if (not isinstance(u, (int, float, Complex, Matrix, Vector)) or
            not isinstance(v, (int, float, Complex, Matrix, Vector))):
        raise AssertionError("lerp: u and v must be int, float, Complex, Matrix or Vector")
    if type(u) is not type(v):
        raise AssertionError("lerp: u and v must have same type.")
    if not isinstance(t, (float, int)) or not 0 <= t <= 1:
        raise AssertionError("lerp: t must be a float between 0 and 1.")
    else:
        t = float(t)

    u += (v - u) * t

    return u


def main():
    try:
        print(lerp(0., 1., 0.))
    except Exception as e:
        print(e)
    print()

    try:
        print(lerp(0, 1, 1))
    except Exception as e:
        print(e)
    print()

    try:
        print(lerp(0., 1., 0.5))
    except Exception as e:
        print(e)
    print()

    try:
        print(lerp(21, 42, 0.3))
    except Exception as e:
        print(e)
    print()

    try:
        print(lerp(Vector([2, 1]), Vector([4, 2]), 0.3))
    except Exception as e:
        print(e)
    print()

    try:
        print(lerp(Matrix([[2, 1], [3, 4]]), Matrix([[20, 10], [30, 40]]), 0.5))
    except Exception as e:
        print(e)
    print()

    # Exceptions
    try:
        print(lerp("Test", "yes", 0.5))
    except Exception as e:
        print(e)
    print()

    try:
        print(lerp(20, Complex(5, 4), 1))
    except Exception as e:
        print(e)
    print()

    try:
        print(lerp(3, 7, 1.3))
    except Exception as e:
        print(e)
    print()

    try:
        print(lerp(3, 17, -0.9))
    except Exception as e:
        print(e)
    print()


if __name__ == "__main__":
    main()
