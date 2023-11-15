from complex_created.complex import Complex
from complex_created.vector import Vector


def main():
    u = Vector([0, 0])
    v = Vector([1, 1])
    print(u.dot(v))
    print()

    u = Vector([1, 1])
    v = Vector([1, 1])
    print(u.dot(v))
    print()

    u = Vector([-1, 6])
    v = Vector([3, 2])
    print(u.dot(v))
    print()

    u = Vector([0.5, 0.25])
    v = Vector([2, -4])
    print(u.dot(v))
    print()

    # Complex
    u = Vector([Complex(2, 1), Complex(3, 4), Complex(3, -1)])
    v = Vector([1, 2, 5])
    print(u.dot(v))
    print()

    # Exceptions
    u = Vector([0, 0])
    print(u.dot("test"))
    print()

    u = Vector([0, 0])
    v = Vector([1, 1, 8])
    print(u.dot(v))
    print()


if __name__ == "__main__":
    main()
