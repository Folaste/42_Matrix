# from vector import Vector
from matrix import Matrix


def main():
    # try:
    # except AssertionError as e:
    #     print(e)
    try:
        a = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        b = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 1, 1]])
        print(a + b)
    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()
