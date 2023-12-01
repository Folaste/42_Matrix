"""
    Exercise 07: Linear Map, Matrix multiplication
"""

from complex import Complex
from matrix import Matrix
from vector import Vector


def main():
    a = Matrix([[1, 2], [3, 4], [5, 6]])
    b = Matrix([[1, 2, 3], [4, 5, 6]])
    print(a)
    print(b)
    print(a * b)
    print(b * a)

    a = Matrix([[1, 2, 3], [4, 5, 6]])
    b = Vector([3, -1])
    print(a)
    print(b)
    print(a * b)

    a = Matrix([[1, 2, 3], [4, 5, 6]])
    b = Matrix([[1, 2], [3, 4], [5, 6], [7, 8]])
    print(a)
    print(b)
    print(a * b)
    print(b * a)

    a = Matrix([[Complex(1, 2), Complex(3, 4)], [Complex(5, 6), Complex(7, 8)]])
    b = Matrix([[Complex(8, 7), Complex(6, 5)], [Complex(4, 3), Complex(2, 1)]])
    print(a)
    print(b)
    print(a * b)
    print(b * a)


if __name__ == "__main__":
    main()
