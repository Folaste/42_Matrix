"""
    Exercise 09: Transpose
"""

from matrix import Matrix


def main():
    try:
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

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
