"""
    Exercise 05: Cosine
"""

from vector import Vector
from ft_math import Re


def angle_cos(u: Vector, v: Vector) -> float:
    """ Return cosine value for the angle define by u and v."""
    # Time complexity: O(1)
    # Space complexity: O(1)
    if u.dim() != v.dim() or u.norm() == 0 or v.norm() == 0:
        raise AssertionError("This expression cannot be calculated")
    return Re((u * v) / (u.norm() * v.norm()))


def main():
    try:
        u = Vector([1, 0])
        v = Vector([1, 0])
        print(angle_cos(u, v))  # 1
        print()

        u = Vector([1, 0])
        v = Vector([0, 1])
        print(angle_cos(u, v))  # 0
        print()

        u = Vector([-1., 1.])
        v = Vector([1., -1.])
        print(angle_cos(u, v))  # -1
        print()

        u = Vector([2., 1.])
        v = Vector([4., 2.])
        print(angle_cos(u, v))  # 1
        print()

        u = Vector([1, 2, 3])
        v = Vector([4, 5, 6])
        print(angle_cos(u, v))  # 0.974631846
        print()

        # Exceptions
        u = Vector([0, 0])
        v = Vector([1., 1.])
        print(angle_cos(u, v))
        print()

        u = Vector([2., 1., 3.])
        v = Vector([4., 2.])
        print(angle_cos(u, v))
        print()

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
