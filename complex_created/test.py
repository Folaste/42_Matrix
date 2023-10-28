from complex import Complex
from matrix import Matrix
from vector import Vector




def main():
    vect = Matrix([[Complex(1, 2), Complex(2, 1)], [Complex(1, 2), Complex(2, 1)]])
    print(str(vect))
    print(repr(vect))


if __name__ == "__main__":
    main()
