"""
    Exercise 12: Inverse
"""

from matrix import Matrix


def main():
    a = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    print(a)
    print(a.inverse())

    a = Matrix([[2, 0, 0], [0, 2, 0], [0, 0, 2]])
    print(a)
    print(a.inverse())

    a = Matrix([[8, 4, 7], [5, 7, 6], [-2, 20, 1]])
    print(a)
    print(a.inverse())

    # Exceptions
    a = Matrix([[1, 2, 3], [4, 5, 6]])
    print(a)
    print(a.inverse())

    a = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(a)
    print(a.inverse())


if __name__ == '__main__':
    main()
