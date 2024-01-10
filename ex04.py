"""
    Exercise 04: Norm
"""

from vector import Vector


def main():
    try:
        u = Vector([0., 0., 0.])
        print(f"{u.norm_1()}, {u.norm()}, {u.norm_inf()}")

        u = Vector([1., 2., 3.])
        print(f"{u.norm_1()}, {u.norm()}, {u.norm_inf()}")

        u = Vector([-1., -2.])
        print(f"{u.norm_1()}, {u.norm()}, {u.norm_inf()}")

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
