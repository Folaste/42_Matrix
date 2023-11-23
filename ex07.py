"""
    Exercise 07: Linear Map, Matrix multiplication
"""

from complex_created.complex import Complex
from complex_created.matrix import Matrix
from complex_created.vector import Vector


def main():
    a = Matrix([[1, 2], [3, 4], [5, 6]])
    b = Matrix([[1, 2, 3], [4, 5, 6]])
    print(a, end="\n\n")
    print(b, end="\n\n")
    print(a * b, end="\n\n")
    print(b * a, end="\n\n")

    a = Matrix([[1, 2, 3], [4, 5, 6]])
    b = Vector([3, -1])
    print(a, end="\n\n")
    print(b, end="\n\n")
    print(a * b, end="\n\n")

    a = Matrix([[1, 2, 3], [4, 5, 6]])
    b = Matrix([[1, 2], [3, 4], [5, 6], [7, 8]])
    print(a, end="\n\n")
    print(b, end="\n\n")
    print(a * b, end="\n\n")
    print(b * a, end="\n\n")

    a = Matrix([[Complex(1, 2), Complex(3, 4)], [Complex(5, 6), Complex(7, 8)]])
    b = Matrix([[Complex(8, 7), Complex(6, 5)], [Complex(4, 3), Complex(2, 1)]])
    print(a, end="\n\n")
    print(b, end="\n\n")
    print(a * b, end="\n\n")
    print(b * a, end="\n\n")


if __name__ == "__main__":
    main()
