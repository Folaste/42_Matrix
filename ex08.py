"""
    Exercise 08: Trace
"""

from complex_created.complex import Complex
from complex_created.matrix import Matrix


def main():
    a = Matrix([[1, 2], [3, 4]])
    print(a)
    print(a.trace(), end="\n\n")

    a = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    print(a)
    print(a.trace(), end="\n\n")

    a = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(a)
    print(a.trace(), end="\n\n")

    a = Matrix([[2, -5, 0], [4, 3, 7], [-2, 3, 4]])
    print(a)
    print(a.trace(), end="\n\n")

    a = Matrix([[-2, -8, 4], [1, -23, 4], [0, 6, 4]])
    print(a)
    print(a.trace(), end="\n\n")

    a = Matrix([[Complex(1, 2), Complex(3, 4)], [Complex(5, 6), Complex(7, 8)]])
    print(a)
    print(a.trace(), end="\n\n")

    a = Matrix([[1, 2, 3], [4, 5, 6]])
    print(a)
    print(a.trace(), end="\n\n")


if __name__ == "__main__":
    main()
