"""
    Exercise 08: Trace
"""

from complex import Complex
from matrix import Matrix


def main():
    a = Matrix([[1, 2], [3, 4]])
    print(a)
    print(a.trace())

    a = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    print(a)
    print(a.trace())

    a = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(a)
    print(a.trace())

    a = Matrix([[2, -5, 0], [4, 3, 7], [-2, 3, 4]])
    print(a)
    print(a.trace())

    a = Matrix([[-2, -8, 4], [1, -23, 4], [0, 6, 4]])
    print(a)
    print(a.trace())

    a = Matrix([[Complex(1, 2), Complex(3, 4)], [Complex(5, 6), Complex(7, 8)]])
    print(a)
    print(a.trace())

    a = Matrix([[1, 2, 3], [4, 5, 6]])
    print(a)
    print(a.trace())


if __name__ == "__main__":
    main()
