from vector import Vector
from matrix import Matrix


def main():
    try:
        vect_c = Vector([2.5 + 2j, 2 - 1j])
        print(vect_c)
    except AssertionError as e:
        print(e)
    print()
    try:
        vect_c = Vector([2.5 + 2j, 2, 1j])
        print(vect_c)
    except AssertionError as e:
        print(e)
    print()
    try:
        vect = Vector([1, 98, 65, 2, 6])
        print(vect)
    except AssertionError as e:
        print(e)
    print()
    try:
        test = Vector([1, "Oui", False], [])
        print(test)
    except AssertionError as e:
        print(e)
    print()
    try:
        test = Matrix([[7, 2], [7, 2]])
        print(test)
    except AssertionError as e:
        print(e)
    print()


if __name__ == "__main__":
    main()
