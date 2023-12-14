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
    try:
        if (not isinstance(u, (int, float, Complex, Matrix, Vector)) or
                not isinstance(v, (int, float, Complex, Matrix, Vector))):
            raise AssertionError("u and v must be int, float, Complex, Matrix or Vector")
        if type(u) is not type(v):
            raise AssertionError("u and v must have same type.")
        if not isinstance(t, (float, int)) or not 0 <= t <= 1:
            raise AssertionError("t must be a float between 0 and 1.")
        else:
            t = float(t)

        u += (v - u) * t

        return u

    except AssertionError as e:
        print(e)
    except TypeError:
        print("Cannot calculate linear interpolation between u and v.")


def main():
    print(lerp(0., 1., 0.))
    print()

    print(lerp(0, 1, 1))
    print()

    print(lerp(0., 1., 0.5))
    print()

    print(lerp(21, 42, 0.3))
    print()

    print(lerp(Vector([2, 1]), Vector([4, 2, 4]), 0.3))
    print()

    print(lerp(Matrix([[2, 1], [3, 4]]), Matrix([[20, 10], [30, 40]]), 0.5))
    print()

    # Exceptions
    print(lerp("Test", "yes", 0.5))
    print()

    print(lerp(20, Complex(5, 4), 1))
    print()

    print(lerp(3, 7, 1.3))
    print()

    print(lerp(3, 17, -0.9))
    print()


if __name__ == "__main__":
    main()
