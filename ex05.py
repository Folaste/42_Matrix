"""
    Exercise 05: Cosine
"""

from complex import Complex
from vector import Vector
from ft_math import Re


def cosine(u: Vector, v: Vector) -> float:
    """ Return cosine value for the angle define by u and v."""
    try:
        if u.dim() != v.dim() or u.norm() == 0 or v.norm() == 0:
            raise AssertionError("This expression cannot be calculated")
        return Re((u * v) / (u.norm() * v.norm()))

    except AssertionError as e:
        print(e)


def main():
    u = Vector([1, 0])
    v = Vector([1, 0])
    print(cosine(u, v))  # 0
    print()

    u = Vector([1, 0])
    v = Vector([0, 1])
    print(cosine(u, v))  # 1
    print()

    u = Vector([-1., 1.])
    v = Vector([1., -1.])
    print(cosine(u, v))  # -1
    print()

    u = Vector([2., 1.])
    v = Vector([4., 2.])
    print(cosine(u, v))  # 1
    print()

    u = Vector([1, 2, 3])
    v = Vector([4, 5, 6])
    print(cosine(u, v))  # 0.974631846
    print()

    u = Vector([Complex(1, 0), Complex(0, 0)])
    v = Vector([Complex(1, 0), Complex(0, 0)])
    print(cosine(u, v))
    print()

    u = Vector([0, 0])
    v = Vector([1., 1.])
    print(cosine(u, v))
    print()

    u = Vector([2., 1., 3.])
    v = Vector([4., 2.])
    print(cosine(u, v))
    print()


if __name__ == "__main__":
    main()
