from complex import Complex
from matrix import Matrix
from vector import Vector


def main():
    a = Matrix([[1, 2, 3], [4, 5, 6]])
    vect = a.to_vector()
    print(a)
    print(vect)
    new = vect.to_matrix(3,2)
    print(new)


if __name__ == "__main__":
    main()
