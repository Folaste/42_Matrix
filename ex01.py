"""
    Exercise 01: Linear Combination
"""


from complex_created.complex import Complex
from complex_created.vector import Vector


def linear_combination(u: list[Vector], coefs: list[int | float | Complex]) -> Vector:
    """ Returns linear combination of vectors u and scalar coefficients coefs. """
    try:
        if len(u) != len(coefs):
            raise AssertionError("u and coefs must have same length.")
        if not all(isinstance(coef, (int, float, Complex)) for coef in coefs):
            raise AssertionError("Numbers in coefs must be int, float or complex.")
        if not all(isinstance(vect, Vector) for vect in u):
            raise AssertionError("Objects in u must be Vectors")

        ret = Vector([0 for _ in range(u[0].dim())])

        for i in range(len(u)):
            ret += u[i] * (coefs[i])

        return ret

    except AssertionError as e:
        print(e)


def main():
    e1 = Vector([1., 0., 0.])
    e2 = Vector([0., 1., 0.])
    e3 = Vector([0., 0., 1.])

    v1 = Vector([1., 2., 3.])
    v2 = Vector([0., 10., -100.])

    print(linear_combination([e1, e2, e3], [10., -2., 0.5]))
    print(linear_combination([v1, v2], [10., -2.]))

    # Exceptions
    print(linear_combination([1, 2, 3], [3, 2, 1]))
    print()

    print(linear_combination([e1, e2, e3], ["test", 2, 1]))
    print()

    print(linear_combination([e1, e2, e3], [-10, 2]))


if __name__ == "__main__":
    main()
