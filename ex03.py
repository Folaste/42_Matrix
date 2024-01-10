"""
    Exercise 03: Dot product
"""

from vector import Vector


def main():
    try:
        u = Vector([0, 0])
        v = Vector([1, 1])
        print(u * v)
        print()

        u = Vector([1, 1])
        v = Vector([1, 1])
        print(u * v)
        print()

        u = Vector([-1, 6])
        v = Vector([3, 2])
        print(u * v)
        print()

        u = Vector([0.5, 0.25])
        v = Vector([2, -4])
        print(u * v)
        print()

        # Exceptions
        u = Vector([0, 0])
        print(u * "test")
        print()

        u = Vector([0, 0])
        v = Vector([1, 1, 8])
        print(u * v)
        print()

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
