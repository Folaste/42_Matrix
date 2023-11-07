from complex_builtin.matrix import Matrix as B_Matrix
from complex_builtin.vector import Vector as B_Vector
# from complex_created.matrix import Matrix as C_Matrix
# from complex_created.vector import Vector as C_Vector
# from complex_created.complex import Complex


def main():
    print("\x1b[31mComplex built-in\x1b[0m")
    print("\x1b[34mVector\x1b[0m")
    print()
    # Not a list
    try:
        vect = B_Vector(2 + 1j)
        print(vect)
    except AssertionError as e:
        print(e)
    print()
    # More than 1 element
    try:
        vect = B_Vector([2, 1, 2], 1, 2)
        print(vect)
    except AssertionError as e:
        print(e)
    print()
    # List in a list
    try:
        vect = B_Vector([[2, 1, 3]])
        print(vect)
    except AssertionError as e:
        print(e)
    print()
    # Have complex and real numbers
    try:
        vect = B_Vector([2 + 1j, 3])
        print(vect)
    except AssertionError as e:
        print(e)
    print()
    print("\x1b[34mMatrix\x1b[0m")
    print()
    # Not a list
    try:
        mat = B_Matrix(2)
        print(mat)
    except AssertionError as e:
        print(e)
    print()
    # As a vector
    try:
        mat = B_Matrix([2, 1])
        print(mat)
    except AssertionError as e:
        print(e)
    print()
    # List in a list in a list
    try:
        mat = B_Matrix([[[2, 1], [1, 2]]])
        print(mat)
    except AssertionError as e:
        print(e)
    print()
    # Empty list
    try:
        mat = B_Matrix([])
        print(mat)
    except AssertionError as e:
        print(e)
    print()
    # Rows haven't same size
    try:
        mat = B_Matrix([[1, 2, 3], [4, 5]])
        print(mat)
    except AssertionError as e:
        print(e)
    print()
    # #
    # try:
    #     mat =
    #     print(mat)
    # except AssertionError as e:
    #     print(e)
    # print()
    # #
    # try:
    #     mat =
    #     print(mat)
    # except AssertionError as e:
    #     print(e)
    # print()
    # #
    # try:
    #     mat =
    #     print(mat)
    # except AssertionError as e:
    #     print(e)
    # print()
    # #
    # try:
    #     mat =
    #     print(mat)
    # except AssertionError as e:
    #     print(e)
    # print()


if __name__ == "__main__":
    main()
