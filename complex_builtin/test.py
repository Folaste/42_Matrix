# from vector import Vector
from matrix import Matrix


def main():
    # try:
    # except AssertionError as e:
    #     print(e)
    try:
        a = Matrix([[1, 2, 3], [4, 5, 6]])
        vect = a.to_vector()
        print(a)
        print(vect)
        new = vect.to_matrix(3, 2)
        print(new)
    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()
