"""
    Exercise 15: Bonus: Complex Vector Spaces
"""

from complex import Complex
from matrix import Matrix
from vector import Vector


def ex01():
    from ex01 import linear_combination
    e1 = Vector([Complex(1, 2), Complex(0, 1), Complex(0, 3)])
    e2 = Vector([Complex(0, -1), Complex(1, 0), Complex(0, 0)])

    print(linear_combination([e1, e2], [Complex(1, 1), Complex(0, 1)]))
    print(linear_combination([e1, e2], [12, 4]))


def ex02():
    from ex02 import lerp
    print(lerp(Complex(3, 1), Complex(9, 14), 0.2), end="\n\n")

    print(lerp(Vector([Complex(3, 1), Complex(9, 14)]), Vector([Complex(1, 2), Complex(0, 1)]), 0.7), end="\n\n")


def ex03():
    u = Vector([Complex(2, 1), Complex(3, 4), Complex(3, -1)])
    v = Vector([1, 2, 5])
    print(f"u =\n{u}")
    print(f"v =\n{v}")
    print(u * v)
    print()

    u = Vector([Complex(-2, 1), Complex(3, 1), Complex(6, -1)])
    v = Vector([Complex(1, 2), Complex(0, 1), Complex(1, 0)])
    print(f"u =\n{u}")
    print(f"v =\n{v}")
    print(u * v)
    print()


def ex04():
    u = Vector([Complex(2, 1), Complex(4, 3), Complex(-3, -2)])
    print(f"u = \n{u}")
    print(f"{u.norm_1()}, {u.norm()}, {u.norm_inf()}")


def ex05():
    from ex05 import angle_cos
    u = Vector([Complex(1, 0), Complex(0, 0)])
    v = Vector([Complex(1, 0), Complex(0, 0)])
    print(f"u =\n{u}")
    print(f"v =\n{v}")
    print(angle_cos(u, v))
    print()


def ex06():
    from ex06 import cross_product
    u = Vector([Complex(1, 0), Complex(2, 1), Complex(1, 2)])
    v = Vector([4, 7, 12])
    print(cross_product(u, v))

    v = Vector([Complex(9, -3), Complex(5, 2), Complex(-1, -2)])
    print(cross_product(u, v))


def ex07():
    a = Matrix([[Complex(1, 2), Complex(3, 4)], [Complex(5, 6), Complex(7, 8)]])
    b = Matrix([[Complex(8, 7), Complex(6, 5)], [Complex(4, 3), Complex(2, 1)]])
    print(f"A = \n{a}")
    print(f"B = \n{b}")
    print(f"A * B =\n{a * b}")
    print(f"B * A =\n{b * a}")


def ex08():
    a = Matrix([[Complex(1, 2), Complex(3, 4)], [Complex(5, 6), Complex(7, 8)]])
    print(a)
    print(a.trace())


def ex09():
    a = Matrix([[Complex(1, 2), Complex(3, 4)], [Complex(5, 6), Complex(7, 8)]])
    print(f'a =\n{a}')
    print(f'aT =\n{a.transpose()}')


def ex10():
    a = Matrix([[Complex(2, 1), Complex(3, 4), Complex(3, -1)],
                [Complex(1, 2), Complex(2, 1), Complex(3, 4)],
                [Complex(3, 4), Complex(3, -1), Complex(1, 2)]])
    print(a)
    print(a.row_echelon())


def ex11():
    a = Matrix([[Complex(2, 1), Complex(3, 4), Complex(3, -1)],
                [Complex(1, 2), Complex(2, 1), Complex(3, 4)],
                [Complex(3, 4), Complex(3, -1), Complex(1, 2)]])
    print(a)
    print(a.determinant(), end="\n\n")


def ex12():
    a = Matrix([[Complex(2, 1), Complex(3, 4), Complex(3, -1)],
                [Complex(1, 2), Complex(2, 1), Complex(3, 4)],
                [Complex(3, 4), Complex(3, -1), Complex(1, 2)]])
    print(a)
    print(a.inverse())


def ex13():
    a = Matrix([[Complex(1, 2), Complex(2, 3)], [Complex(3, 4), Complex(4, 5)]])
    print(a)
    print(f"Rank = {a.rank()}", end="\n\n")


def main():
    print("### EX01: Linear Combination ###\n")
    ex01()
    print()

    print("### EX02: Linear Interpolation ###\n")
    ex02()
    print()

    print("### EX03: Scalar Product ###\n")
    ex03()
    print()

    print("### EX04: Norm ###\n")
    ex04()
    print()

    print("### EX05: Cosine ###\n")
    ex05()
    print()

    print("### EX06: Cross Product ###\n")
    ex06()
    print()

    print("### EX07: Matrix Multiplication ###\n")
    ex07()
    print()

    print("### EX08: Trace ###\n")
    ex08()
    print()

    print("### EX09: Transpose ###\n")
    ex09()
    print()

    print("### EX10: Row Echelon Form ###\n")
    ex10()
    print()

    print("### EX11: Determinant ###\n")
    ex11()
    print()

    print("### EX12: Inverse ###\n")
    ex12()
    print()

    print("### EX13: Rank ###\n")
    ex13()
    print()


if __name__ == '__main__':
    main()
