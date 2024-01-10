"""
    Exercise 11: Determinant
"""

from matrix import Matrix


def main():
    try:
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

        # Exceptions
        a = Matrix([[1, 2], [3, 4], [5, 6]])
        print(a)
        print(a.determinant(), end="\n\n")

        a = Matrix([[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4], [5, 5, 5, 5, 5]])
        print(a)
        print(a.determinant())

    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
