"""
    Exercise 00: Add, Subtract and Scale
"""


from complex_builtin.matrix import Matrix as B_Matrix
from complex_builtin.vector import Vector as B_Vector

from complex_created.complex import Complex
from complex_created.matrix import Matrix as C_Matrix
from complex_created.vector import Vector as C_Vector


def vector_builtin():
    print("\x1b[31m~ Vector with type complex builtin ~\x1b[0m")
    print("\x1b[34m# Addition #\x1b[0m")
    print()

    print("\x1b[32m| Real + Real |\x1b[0m")
    try:
        a = B_Vector([1, 2, 3])
        b = B_Vector([4, 5, 6])

        c = a + b
        print(c)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m| Real + Complex |\x1b[0m")
    try:
        a = B_Vector([1, 2])
        b = B_Vector([4 + 1j, 5 + 6j])

        a += b
        print(a)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m| Complex + Complex |\x1b[0m")
    try:
        a = B_Vector([1 + 2j, 2 - 1j, 3 - 2j, 1 - 2j])
        b = B_Vector([4 - 2j, 5 + 2j, 6 - 3j, 4 + 5j])

        a += b
        print(a)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m| Exception: Different size |\x1b[0m")
    try:
        a = B_Vector([1 + 2j, 2 - 1j, 3 - 2j, 1 - 2j])
        b = B_Vector([4 - 2j, 5 + 2j, 6 - 3j])

        a += b
        print(a)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[34m# Subtraction #\x1b[0m")

    print("\x1b[32m| Real - Real |\x1b[0m")
    try:
        a = B_Vector([4, 2])
        b = B_Vector([1, 3])

        c = a - b
        print(c)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m| Complex - Complex |\x1b[0m")
    try:
        a = B_Vector([2 - 1j, 2 + 1j])
        b = B_Vector([1 + 3j, 5 - 2j])

        c = a - b
        print(c)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m| Complex - Real |\x1b[0m")
    try:
        a = B_Vector([2 - 1j, 2 + 1j, 9 + 0j])
        b = B_Vector([7, 5, 1])

        c = a - b
        print(c)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m| Real - Complex |\x1b[0m")
    try:
        a = B_Vector([4, 1, 6])
        b = B_Vector([1 + 3j, 5 - 2j, 4 + 5j])

        c = a - b
        print(c)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m| Exception: Different size |\x1b[0m")
    try:
        a = B_Vector([4, 1, 6])
        b = B_Vector([1 + 3j, 5 - 2j])

        c = a - b
        print(c)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[34m# Scalar Multiplication #\x1b[0m")

    print("\x1b[32m| Real Scalar * Real Vector |\x1b[0m")
    try:
        a = B_Vector([2, 5, 7])
        c = a * 3
        print(c)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m| Complex Scalar * Real Vector |\x1b[0m")
    try:
        a = B_Vector([1, 5])
        c = a * (9 + 2j)
        print(c)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m| Real Scalar * Complex Vector |\x1b[0m")
    try:
        a = B_Vector([1 + 2j, 5 - 3j])
        c = a * 8
        print(c)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m| Complex Scalar * Complex Vector |\x1b[0m")
    try:
        a = B_Vector([1 + 2j, 5 - 3j])
        c = a * (2 + 5j)
        print(c)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m| Exception: Not a Number Scalar |\x1b[0m")
    try:
        a = B_Vector([1, 5, 12])
        c = a * "Test"
        print(c)
    except AssertionError as e:
        print(e)
    print()


def matrix_builtin():
    print("\x1b[31m~ Matrix with type complex builtin ~\x1b[0m")
    print("\x1b[34m# Addition #\x1b[0m")
    print()

    print("\x1b[32m| Real + Real |\x1b[0m")
    try:
        a = B_Matrix([[1, 2], [3, 4]])
        b = B_Matrix([[2, 2], [2, 2]])

        c = a + b
        print(c)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m| Complex + Real |\x1b[0m")
    try:
        a = B_Matrix([[1 - 1j, 2 + 4j], [3 + 2j, 4 - 3j], [5 + 2j, 2 + 3j]])
        b = B_Matrix([[2, 2], [2, 2], [3, 3]])

        c = a + b
        print(c)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m| Complex + Complex |\x1b[0m")
    try:
        a = B_Matrix([[1 - 1j, 2 + 4j, 3 + 2j], [4 - 3j, 5 + 2j, 2 + 3j]])
        b = B_Matrix([[7 - 2j, 2 + 1j, 2 - 5j], [9 - 4j, 3 + 4j, 8 - 3j]])

        c = a + b
        print(c)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m| Exception: Different shapes |\x1b[0m")
    try:
        a = B_Matrix([[1 - 1j, 2 + 4j], [3 + 2j, 4 - 3j]])
        b = B_Matrix([[2, 2], [2, 2], [3.2, 3]])

        c = a + b
        print(c)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[34m# Subtraction #\x1b[0m")
    
    print("\x1b[32m| Real - Real |\x1b[0m")
    try:
        a = B_Matrix([[1, 2], [3, 4], [5, 2]])
        b = B_Matrix([[2, 2], [2.0, 2], [3, 3]])

        c = a - b
        print(c)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m| Complex - Real |\x1b[0m")
    try:
        a = B_Matrix([[1 - 1j, 2 + 4j], [3 + 2j, 4 - 3j]])
        b = B_Matrix([[2, 2], [2, 2.4]])

        c = a - b
        print(c)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m| Real - Complex |\x1b[0m")
    try:
        a = B_Matrix([[5, 3, 3.3], [8, 2, 1]])
        b = B_Matrix([[3 + 2j, 4 - 4j, 1 - 6j], [5 - 2j, 9 + 5j, 7 - 4j]])

        c = a - b
        print(c)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m| Complex - Complex |\x1b[0m")
    try:
        a = B_Matrix([[5 - 4j, 3 + 2j, 3 - 9j], [8 + 4j, 2 - 9j, 1 + 0j]])
        b = B_Matrix([[3 + 2j, 4 - 4j, 1 - 6j], [5 - 2j, 9 + 5j, 7 - 4j]])

        c = a - b
        print(c)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m| Exception: Different shapes |\x1b[0m")
    try:
        a = B_Matrix([[5 - 4j, 3 + 2j, 3 - 9j], [8 + 4j, 2 - 9j, 1 + 0j]])
        b = B_Matrix([[3 + 2j, 4 - 4j], [5 - 2j, 9 + 5j]])

        c = a - b
        print(c)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[34m# Scalar Multiplication #\x1b[0m")

    print("\x1b[32m| Real Scalar * Real Matrix |\x1b[0m")
    try:
        a = B_Matrix([[4, 23, 3], [1, -4, 6.1], [5, 2, -4]])
        c = a * 4
        print(c)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m| Complex Scalar * Real Matrix |\x1b[0m")
    try:
        a = B_Matrix([[6, 3, -5], [1, -4, 6], [5, 0, -4]])
        c = a * (3 + 2j)
        print(c)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m| Real Scalar * Complex Matrix |\x1b[0m")
    try:
        a = B_Matrix([[4 + 2j, 3 - 1j], [-4 + 6j, 5 - 2j]])
        c = a * 4
        print(c)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m| Complex Scalar * Complex Matrix |\x1b[0m")
    try:
        a = B_Matrix([[4 + 2j, 3 - 1j], [-4 + 6j, 5 - 2j]])
        c = a * (1 + 2j)
        print(c)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m| Exception: Not a number scalar |\x1b[0m")
    try:
        a = B_Matrix([[4, 1], [-4, 5]])
        c = a * True
        print(c)
    except AssertionError as e:
        print(e)
    print()


def vector_created():
    print("\x1b[31m~ Vector with type complex created ~\x1b[0m")
    print("\x1b[34m# Addition #\x1b[0m")
    print()

    print("\x1b[32m| Real + Real |\x1b[0m")
    try:
        a = C_Vector([1, 2, 3])
        b = C_Vector([4, 5, 6])

        c = a + b
        print(c)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m| Real + Complex |\x1b[0m")
    try:
        a = C_Vector([1, 2])
        b = C_Vector([Complex(4, 1), Complex(5, 6)])

        a += b
        print(a)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m| Complex + Complex |\x1b[0m")
    try:
        a = C_Vector([Complex(1, 2), Complex(2, -1), Complex(3, -2), Complex(1, -2)])
        b = C_Vector([Complex(4, -2), Complex(5, 2), Complex(6, -3), Complex(4, 5)])

        a += b
        print(a)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m| Exception: Different size |\x1b[0m")
    try:
        a = C_Vector([Complex(1, 2), Complex(2, -1), Complex(3, -2), Complex(1, -2)])
        b = C_Vector([5, 8, 3])

        a += b
        print(a)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[34m# Subtraction #\x1b[0m")

    print("\x1b[32m| Real - Real |\x1b[0m")
    try:
        a = C_Vector([4, 2])
        b = C_Vector([1, 3])

        c = a - b
        print(c)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m| Complex - Complex |\x1b[0m")
    try:
        a = C_Vector([Complex(2, -1), Complex(2, 1)])
        b = C_Vector([Complex(1, 3), Complex(5, -2)])

        c = a - b
        print(c)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m| Complex - Real |\x1b[0m")
    try:
        a = C_Vector([Complex(2, -1), Complex(2, 1), Complex(9, 0)])
        b = C_Vector([7, 5, 1])

        c = a - b
        print(c)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m| Real - Complex |\x1b[0m")
    try:
        a = C_Vector([4, 1, 6])
        b = C_Vector([Complex(1, 3), Complex(5, -2), Complex(5, 2)])

        c = a - b
        print(c)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m| Exception: Different size |\x1b[0m")
    try:
        a = C_Vector([4, 1, 6])
        b = C_Vector([Complex(1, 3), Complex(5, -2)])

        c = a - b
        print(c)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[34m# Scalar Multiplication #\x1b[0m")

    print("\x1b[32m| Real Scalar * Real Vector |\x1b[0m")
    try:
        a = C_Vector([2, 5, 7])
        c = a * 3
        print(c)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m| Complex Scalar * Real Vector |\x1b[0m")
    try:
        a = C_Vector([1, 5])
        c = a * Complex(9, 2)
        print(c)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m| Real Scalar * Complex Vector |\x1b[0m")
    try:
        a = C_Vector([Complex(1, 2), Complex(5, -3)])
        c = a * 8
        print(c)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m| Complex Scalar * Complex Vector |\x1b[0m")
    try:
        a = C_Vector([Complex(1, 2), Complex(5, -3)])
        c = a * Complex(2, 5)
        print(c)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m| Exception: Not a Number Scalar |\x1b[0m")
    try:
        a = C_Vector([1, 5, 12])
        c = a * "Test"
        print(c)
    except AssertionError as e:
        print(e)
    print()


def matrix_created():
    print("\x1b[31m~ Matrix with type complex created ~\x1b[0m")
    print("\x1b[34m# Addition #\x1b[0m")
    print()

    print("\x1b[32m| Real + Real |\x1b[0m")
    try:
        a = C_Matrix([[1, 2], [3, 4]])
        b = C_Matrix([[2, 2], [2, 2]])

        c = a + b
        print(c)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m| Complex + Real |\x1b[0m")
    try:
        a = C_Matrix([[Complex(1, -1), Complex(2, 4)],
                      [Complex(3, 2), Complex(4, -3)],
                      [Complex(5, 2), Complex(2, 3)]])
        b = C_Matrix([[2, 2], [2, 2], [3, 3]])

        c = a + b
        print(c)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m| Complex + Complex |\x1b[0m")
    try:
        a = C_Matrix([[Complex(1, -1), Complex(2, 4), Complex(3, 2)],
                      [Complex(4, -3), Complex(5, 2), Complex(2, 3)]])
        b = C_Matrix([[Complex(7, -2), Complex(2, 1), Complex(2, -5)],
                      [Complex(9, -4), Complex(3, 4), Complex(8, -3)]])

        c = a + b
        print(c)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m| Exception: Different shapes |\x1b[0m")
    try:
        a = C_Matrix([[Complex(1, -1), Complex(2, 4)],
                      [Complex(3, 2), Complex(4, -3)]])
        b = C_Matrix([[2, 2], [2, 2], [3.2, 3]])

        c = a + b
        print(c)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[34m# Subtraction #\x1b[0m")

    print("\x1b[32m| Real - Real |\x1b[0m")
    try:
        a = C_Matrix([[1, 2], [3, 4], [5, 2]])
        b = C_Matrix([[2, 2], [2, 2], [3, 3]])

        c = a - b
        print(c)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m| Complex - Real |\x1b[0m")
    try:
        a = C_Matrix([[Complex(1, -1), Complex(2, 4)],
                      [Complex(3, 2), Complex(4, -3)]])
        b = C_Matrix([[2, 2], [2, 2.4]])

        c = a - b
        print(c)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m| Real - Complex |\x1b[0m")
    try:
        a = C_Matrix([[5, 3, 3.3], [8, 2, 1]])
        b = C_Matrix([[Complex(3, 2), Complex(4, -4), Complex(1, -6)],
                      [Complex(5, -2), Complex(9, 5), Complex(7, -4)]])

        c = a - b
        print(c)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m| Complex - Complex |\x1b[0m")
    try:
        a = C_Matrix([[Complex(5, -4), Complex(3, 2), Complex(3, -9)],
                      [Complex(8, 4), Complex(2, -9), Complex(1, 0)]])

        b = C_Matrix([[Complex(3, 2), Complex(4, -4), Complex(1, -6)],
                      [Complex(5, -2), Complex(9, 5), Complex(7, -4)]])

        c = a - b
        print(c)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m| Exception: Different shapes |\x1b[0m")
    try:
        a = C_Matrix([[5, 3, 3], [8, 2, 1]])
        b = C_Matrix([[Complex(3, 2), Complex(4, -4)],
                      [Complex(5, -2), Complex(9, 5)]])

        c = a - b
        print(c)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[34m# Scalar Multiplication #\x1b[0m")

    print("\x1b[32m| Real Scalar * Real Matrix |\x1b[0m")
    try:
        a = C_Matrix([[4, 23, 3], [1, -4, 6.1], [5, 2, -4]])
        c = a * 4
        print(c)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m| Complex Scalar * Real Matrix |\x1b[0m")
    try:
        a = C_Matrix([[6, 3, -5], [1, -4, 6], [5, 0, -4]])
        c = a * Complex(3, 2)
        print(c)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m| Real Scalar * Complex Matrix |\x1b[0m")
    try:
        a = C_Matrix([[Complex(4, 2), Complex(3, -1)],
                      [Complex(-4, 6), Complex(5, -2)]])
        c = a * 4
        print(c)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m| Complex Scalar * Complex Matrix |\x1b[0m")
    try:
        a = C_Matrix([[Complex(4, 2), Complex(3, -1)],
                      [Complex(-4, 6), Complex(5, -2)]])
        c = a * Complex(1, 2)
        print(c)
    except AssertionError as e:
        print(e)
    print()

    print("\x1b[32m| Exception: Not a number scalar |\x1b[0m")
    try:
        a = C_Matrix([[4, 1], [-4, 5]])
        c = a * True
        print(c)
    except AssertionError as e:
        print(e)
    print()


if __name__ == "__main__":
    vector_builtin()
    matrix_builtin()
    print()
    vector_created()
    matrix_created()
