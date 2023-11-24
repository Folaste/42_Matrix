"""
    Exercise 09: Transpose
"""

from complex_created.complex import Complex
from complex_created.matrix import Matrix


def main():
    a = Matrix([[1, 2, 3], [4, 5, 6]])
    print(f'a = \n{a}')
    print(f'aT = \n{a.transpose()}')

    a = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(f'a = \n{a}')
    print(f'aT = \n{a.transpose()}')

    a = Matrix([[1, 2, 3, 4], [5, 6, 7, 8]])
    print(f'a = \n{a}')
    print(f'aT = \n{a.transpose()}')

    a = Matrix([[1, 2], [3, 4], [5, 6], [7, 8]])
    print(f'a = \n{a}')
    print(f'aT = \n{a.transpose()}')

    a = Matrix([[1, 2, 3, 4, 5]])
    print(f'a = \n{a}')
    print(f'aT = \n{a.transpose()}')

    a = Matrix([[Complex(1, 2), Complex(3, 4)], [Complex(5, 6), Complex(7, 8)]])
    print(f'a = \n{a}')
    print(f'aT = \n{a.transpose()}')


if __name__ == "__main__":
    main()
