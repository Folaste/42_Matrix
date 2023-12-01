"""
    Exercise 04: Norm
"""

from complex import Complex
from vector import Vector


def main():
    u = Vector([0., 0., 0.])
    print(f"{u.norm_1()}, {u.norm()}, {u.norm_inf()}")

    u = Vector([1., 2., 3.])
    print(f"{u.norm_1()}, {u.norm()}, {u.norm_inf()}")

    u = Vector([-1., -2.])
    print(f"{u.norm_1()}, {u.norm()}, {u.norm_inf()}")

    u = Vector([Complex(2, 1), Complex(4, 3), Complex(-3, -2)])
    print(f"{u.norm_1()}, {u.norm()}, {u.norm_inf()}")


if __name__ == "__main__":
    main()
