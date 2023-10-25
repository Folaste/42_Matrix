from vector import Vector
from matrix import Matrix


def main():
    try:
        vect = Vector([[2, 2], ["2", 1]])
        print(vect)
        # vect.dim()
    except AssertionError as e:
        print(e)
        exit(1)


if __name__ == "__main__":
    main()
