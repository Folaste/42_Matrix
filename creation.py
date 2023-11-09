from complex_builtin.matrix import Matrix as B_Matrix
from complex_builtin.vector import Vector as B_Vector

from complex_created.matrix import Matrix as C_Matrix
from complex_created.vector import Vector as C_Vector
from complex_created.complex import Complex


def main_builtin():
    print("\x1b[31m~ Complex built-in ~\x1b[0m")
    print("\x1b[34m# Vector #\x1b[0m")
    print()

    print("\x1b[32m- Not a list -\x1b[0m")
    try:
        vect = B_Vector(2 + 1j)
        print(vect)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m- More than 1 element -\x1b[0m")
    try:
        vect = B_Vector([2, 1, 2], 1, 2)
        print(vect)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m- List in a list -\x1b[0m")
    try:
        vect = B_Vector([[2, 1, 3]])
        print(vect)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m- Complex and real numbers -\x1b[0m")
    try:
        vect = B_Vector([2 + 1j, 3])
        print(vect)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[34m# Matrix #\x1b[0m")
    print()

    print("\x1b[32m- Not a list -\x1b[0m")
    try:
        mat = B_Matrix(2)
        print(mat)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m- As a vector -\x1b[0m")
    try:
        mat = B_Matrix([2, 1])
        print(mat)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m- List in a list in a list -\x1b[0m")
    try:
        mat = B_Matrix([[[2, 1], [1, 2]]])
        print(mat)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m- Empty list -\x1b[0m")
    try:
        mat = B_Matrix([])
        print(mat)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m- Different size columns -\x1b[0m")
    try:
        mat = B_Matrix([[1, 2, 3], [4, 5]])
        print(mat)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m- No numbers in columns -\x1b[0m")
    try:
        mat = B_Matrix([["Oui", "Non"], [True, False]])
        print(mat)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m- Empty columns -\x1b[0m")
    try:
        mat = B_Matrix([[], [], []])
        print(mat)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m- In a column, different types -\x1b[0m")
    try:
        mat = B_Matrix([[2 + 1j, 2], [1, 2]])
        print(mat)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m- Columns haven't same types -\x1b[0m")
    try:
        mat = B_Matrix([[2 + 1j, 1 - 1j], [2, 3], [1.2, 4.5]])
        print(mat)
    except AssertionError as e:
        print(e)


def main_created():
    print("\x1b[31m~ Complex created ~\x1b[0m")
    print("\x1b[34m# Complex #\x1b[0m")
    print()

    print("\x1b[32m- 1 element -\x1b[0m")
    try:
        cplx = Complex(1)
        print(cplx)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m- More than 2 elements -\x1b[0m")
    try:
        cplx = Complex(1.5, 2.0, 3.1)
        print(cplx)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m- Constructor without numbers -\x1b[0m")
    try:
        cplx = Complex("Oui", False)
        print(cplx)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[34m# Vector #\x1b[0m")
    print()

    print("\x1b[32m- Not a list -\x1b[0m")
    try:
        vect = C_Vector(Complex(2, 1))
        print(vect)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m- More than 1 element -\x1b[0m")
    try:
        vect = C_Vector([2, 1, 2], 1, 2)
        print(vect)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m- List in a list -\x1b[0m")
    try:
        vect = C_Vector([[2, 1, 3]])
        print(vect)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m- Complex and real numbers -\x1b[0m")
    try:
        vect = C_Vector([Complex(2, -1), 3])
        print(vect)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[34m# Matrix #\x1b[0m")
    print()

    print("\x1b[32m- Not a list -\x1b[0m")
    try:
        mat = C_Matrix(2)
        print(mat)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m- As a vector -\x1b[0m")
    try:
        mat = C_Matrix([2, 1])
        print(mat)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m- List in a list in a list -\x1b[0m")
    try:
        mat = C_Matrix([[[2, 1], [1, 2]]])
        print(mat)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m- Empty list -\x1b[0m")
    try:
        mat = C_Matrix([])
        print(mat)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m- Different size columns -\x1b[0m")
    try:
        mat = C_Matrix([[1, 2, 3], [4, 5]])
        print(mat)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m- No numbers in columns -\x1b[0m")
    try:
        mat = C_Matrix([["Oui", "Non"], [True, False]])
        print(mat)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m- Empty columns -\x1b[0m")
    try:
        mat = C_Matrix([[], [], []])
        print(mat)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m- Multiple types in a column -\x1b[0m")
    try:
        mat = C_Matrix([[Complex(3, 4), 2], [1, 2]])
        print(mat)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m- Columns haven't same type -\x1b[0m")
    try:
        mat = C_Matrix([[Complex(2, 1), Complex(1, -1)], [2, 3], [1.2, 4.5]])
        print(mat)
    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    # main_builtin()
    # print()
    main_created()
