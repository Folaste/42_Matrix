from complex import Complex
from matrix import Matrix
from vector import Vector


def main():
    # matrix = Matrix([[Complex(1, 2), Complex(2, 1)], [Complex(1, 2), Complex(2, 1)]])
    # vect = matrix.to_vector()
    # print(vect)
    # print()
    vector = Vector([1, 2, 3, 4, 5])
    print(vector.scl(3))
    print(repr(vector))
    vector.dim()


if __name__ == "__main__":
    main()
