"""
    Exercise 11: Determinant
"""

from matrix import Matrix
from complex import Complex


def main():
    # a = Matrix([])
    # print(a)
    # print(a.determinant())
    a = Matrix([[1, -1], [-1, 1]])
    print(a)
    print(a.determinant(), end="\n\n")

    a = Matrix([[2, 0, 0], [0, 2, 0], [0, 0, 2]])
    print(a)
    print(a.determinant(), end="\n\n")

    a = Matrix([[8, 4, 7], [5, 7, 6], [-2, 20, 1]])
    print(a)
    print(a.determinant(), end="\n\n")

    a = Matrix([[8, 4, 8, 28], [5, 2.5, 5, -4], [-2, 20, 1, 17], [4, 4, 4, 1]])
    print(a)
    print(a.determinant(), end="\n\n")

    # Complex
    a = Matrix([[Complex(2, 1), Complex(3, 4), Complex(3, -1)],
                [Complex(1, 2), Complex(2, 1), Complex(3, 4)],
                [Complex(3, 4), Complex(3, -1), Complex(1, 2)]])
    print(a)
    print(a.determinant(), end="\n\n")

    # Exceptions
    a = Matrix([[1, 2], [3, 4], [5, 6]])
    print(a)
    print(a.determinant())


if __name__ == '__main__':
    main()
