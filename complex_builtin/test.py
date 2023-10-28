from vector import Vector
from matrix import Matrix


def main():
    try:
        vect_c = Vector([2.5 + 2j, 2 - 1j])
        print(vect_c)
        print(repr(vect_c))
    except AssertionError as e:
        print(e)
    print()
    try:
        vect_c = Vector([2.5 + 2j, 2, 1j])
        print(vect_c)
        vect_c.dim()
    except AssertionError as e:
        print(e)
    print()
    try:
        vect = Vector([1, 98, 65, 2, 6, 5])
        print(vect)
        print()
        mat = vect.to_matrix(2, 3)
        print(mat)
        print()
        vec = mat.to_vector()
        print(vec)
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
        test = Matrix([[7, 2, 5], [7, 2, 1]])
        print(test)
        print(test.shape())
        print(test.is_square())
    except AssertionError as e:
        print(e)
    print()


if __name__ == "__main__":
    main()
