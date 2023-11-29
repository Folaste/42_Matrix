"""
    Exercise 11: Determinant
"""

from complex_created.matrix import Matrix


def main():
    a = Matrix([[8, 4, 8, 28], [5, 2.5, 5, -4], [-2, 20, 1, 17], [4, 4, 4, 1]])
    print(a.determinant())


if __name__ == '__main__':
    main()
