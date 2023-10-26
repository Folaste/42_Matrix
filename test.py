from vector import Vector
from matrix import Matrix


def main():
    try:
        vect_c = Vector([[2.5, 2], [2, -1]])
        vect_c.print()
        vect_c.dim()
        print()
        vect = Vector([1, 98, 65, 2, 6])
        vect.print()
        vect.dim()
        print()
        test = Vector([1, "Oui", False], [])
        test.print()
        test.dim()
    except AssertionError as e:
        print(e)
        exit(1)


if __name__ == "__main__":
    main()
