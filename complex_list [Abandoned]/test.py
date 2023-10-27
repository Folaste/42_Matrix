from vector import Vector
from matrix import Matrix


def main():
    try:
        vect_c = Vector([[2.5, 2], [2, -1]])
        vect_c.print()
        vect_c.dim()
    except AssertionError as e:
        print(e)
    print()
    try:
        vect = Vector([1, 98, 65, 2, 6])
        vect.print()
        vect.dim()
    except AssertionError as e:
        print(e)
    print()
    try:
        test = Vector([1, "Oui", False], [])
        test.print()
        test.dim()
    except AssertionError as e:
        print(e)
    print()
    try:
        test = Matrix([[[5, 6], [1, 2]],
                       [[1, 4], [5, 6.8]]])
        print(test.is_square())
        test.shape()
        print(test.complex)
    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()
    c_nb = 4.7 + 0.2j
    print(type(c_nb))
    print(c_nb)
