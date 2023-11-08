from complex_builtin.matrix import Matrix as B_Matrix
from complex_builtin.vector import Vector as B_Vector
from complex_created.matrix import Matrix as C_Matrix
from complex_created.vector import Vector as C_Vector
from complex_created.complex import Complex


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
    # Columns haven't same size
    try:
        mat = B_Matrix([[1, 2, 3], [4, 5]])
        print(mat)
    except AssertionError as e:
        print(e)
    print()
    # Not numbers in column
    try:
        mat = B_Matrix([["Oui", "Non"], [True, False]])
        print(mat)
    except AssertionError as e:
        print(e)
    print()
    # Empty columns
    try:
        mat = B_Matrix([[], [], []])
        print(mat)
    except AssertionError as e:
        print(e)
    print()
    # In a columns, multiple types
    try:
        mat = B_Matrix([[2 + 1j, 2], [1, 2]])
        print(mat)
    except AssertionError as e:
        print(e)
    print()
    # Columns haven't same types
    try:
        mat = B_Matrix([[2 + 1j, 1 - 1j], [2, 3], [1.2, 4.5]])
        print(mat)
    except AssertionError as e:
        print(e)
    print()
    print("\x1b[31mComplex created\x1b[0m")
    print("\x1b[34mComplex\x1b[0m")
    print()
    # 1 element
    try:
        cplx = Complex(1)
        print(cplx)
    except AssertionError as e:
        print(e)
    print()
    # More than 2 elements
    try:
        cplx = Complex(1.5, 2.0, 3.1)
        print(cplx)
    except AssertionError as e:
        print(e)
    print()
    # Constructor without numbers
    try:
        cplx = Complex("Oui", False)
        print(cplx)
    except AssertionError as e:
        print(e)
    print()
    print("\x1b[34mVector\x1b[0m")
    print()
    # Not a list
    try:
        vect = C_Vector(Complex(2, 1))
        print(vect)
    except AssertionError as e:
        print(e)
    print()
    # More than 1 element
    try:
        vect = C_Vector([2, 1, 2], 1, 2)
        print(vect)
    except AssertionError as e:
        print(e)
    print()
    # List in a list
    try:
        vect = C_Vector([[2, 1, 3]])
        print(vect)
    except AssertionError as e:
        print(e)
    print()
    # Have complex and real numbers
    try:
        vect = C_Vector([Complex(2, -1), 3])
        print(vect)
    except AssertionError as e:
        print(e)
    print()
    print("\x1b[34mMatrix\x1b[0m")
    print()
    # Not a list
    try:
        mat = C_Matrix(2)
        print(mat)
    except AssertionError as e:
        print(e)
    print()
    # As a vector
    try:
        mat = C_Matrix([2, 1])
        print(mat)
    except AssertionError as e:
        print(e)
    print()
    # List in a list in a list
    try:
        mat = C_Matrix([[[2, 1], [1, 2]]])
        print(mat)
    except AssertionError as e:
        print(e)
    print()
    # Empty list
    try:
        mat = C_Matrix([])
        print(mat)
    except AssertionError as e:
        print(e)
    print()
    # Rows haven't same size
    try:
        mat = C_Matrix([[1, 2, 3], [4, 5]])
        print(mat)
    except AssertionError as e:
        print(e)
    print()
    # Not numbers in columns
    try:
        mat = C_Matrix([["Oui", "Non"], [True, False]])
        print(mat)
    except AssertionError as e:
        print(e)
    print()
    # Empty columns
    try:
        mat = C_Matrix([[], [], []])
        print(mat)
    except AssertionError as e:
        print(e)
    print()
    # In a column, multiple types
    try:
        mat = C_Matrix([[Complex(3, 4), 2], [1, 2]])
        print(mat)
    except AssertionError as e:
        print(e)
    print()
    # Columns haven't same types
    try:
        mat = C_Matrix([[Complex(2, 1), Complex(1, -1)], [2, 3], [1.2, 4.5]])
        print(mat)
    except AssertionError as e:
        print(e)
    print()


if __name__ == "__main__":
    main()
