from complex import Complex
from matrix import Matrix
from vector import Vector


def main():
    a = Vector([1.0, 2.0, 3.0])
    b = Vector([1, 2, 3])

    print(a.norm_inf())


if __name__ == "__main__":
    main()
