# from vector import Vector
from matrix import Matrix


def main():
    # try:
    # except AssertionError as e:
    #     print(e)
    try:
        a = Matrix([[1, 1, 1], [1, 1, 1]])
        b = Matrix([[1, 1, 1], [1, 1, 1]])


        print(a, end='\n\n')
        obj = eval(repr(a))

        print(obj)

        print(a - b)
    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()
