"""
    Exercise 10: Row-Echelon Form
"""

from matrix import Matrix


def main():
    a = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    print(a)
    print(a.row_echelon())

    a = Matrix([[1, 3], [2, 4]])
    print(a)
    print(a.row_echelon())

    a = Matrix([[1, 2], [2, 4]])
    print(a)
    print(a.row_echelon())

    a = Matrix([[8, 4, 8], [5, 2.5, 5], [-2, 20, 1], [4, 4, 4], [28, -4, 17]])
    print(a)
    print(a.row_echelon())


if __name__ == "__main__":
    main()
