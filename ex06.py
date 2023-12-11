"""
    Exercise 06: Cross Product
"""

from vector import Vector


def cross_product(u: Vector, v: Vector) -> Vector:
    """ Returns cross product of vectors u and v. """
    # Time complexity: O(1)
    # Space complexity: O(1)
    try:
        if not isinstance(u, Vector) or not isinstance(v, Vector):
            raise TypeError()
        if not u.dim() == v.dim() == 3:
            raise ValueError()
        else:
            return Vector([u[1] * v[2] - u[2] * v[1],
                           u[2] * v[0] - u[0] * v[2],
                           u[0] * v[1] - u[1] * v[0]])

    except TypeError:
        print("u and v must be vectors.")
    except ValueError:
        print("u and v must have 3 dimensions.")


def main():
    u = Vector([0, 0, 1])
    v = Vector([1, 0, 0])
    print(cross_product(u, v))

    u = Vector([1, 2, 3])
    v = Vector([4, 5, 6])
    print(cross_product(u, v))

    u = Vector([4, 2, -3])
    v = Vector([-2, -5, 16])
    print(cross_product(u, v))

    # Exceptions
    u = Vector([1, 2])
    v = Vector([3, 4, 5])
    print(cross_product(u, v))

    u = "Test"
    v = Vector([4, 7, 12])
    print(cross_product(u, v))


if __name__ == "__main__":
    main()
