"""
    Exercise 07: Linear Map, Matrix multiplication
"""

from matrix import Matrix
from vector import Vector


def main():
    try:
        a = Matrix([[1, 2], [3, 4], [5, 6]])
        b = Matrix([[1, 2, 3], [4, 5, 6]])
        print(f"A =\n{a}")
        print(f"B =\n{b}")
        print(f"A * B =\n{a * b}")
        print(f"B * A =\n{b * a}")

        a = Matrix([[1, 2, 3], [4, 5, 6]])
        b = Vector([3, -1])
        print(f"A =\n{a}")
        print(f"B =\n{b}")
        print(f"A * B =\n{a * b}")

        a = Matrix([[1, 2, 3], [4, 5, 6]])
        b = Matrix([[1, 2], [3, 4], [5, 6], [7, 8]])
        print(f"A =\n{a}")
        print(f"B =\n{b}")
        print(f"A * B =\n{a * b}")
        # Exception
        print(f"B * A =")
        print(b * a)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
