"""
    Exercise 13: Rank
"""

from complex import Complex
from matrix import Matrix

def main():
    a = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    print(a)
    print(f"Rank = {a.rank()}", end="\n\n")

    a = Matrix([[1, 2, -1], [2, 4, 2], [0, 0, 1], [0, 0, 1]])
    print(a)
    print(f"Rank = {a.rank()}", end="\n\n")

    a = Matrix([[8, 4, 7, 21], [5, 7, 6, 18], [-2, 20, 1, 7]])
    print(a)
    print(f"Rank = {a.rank()}", end="\n\n")

    # Complex
    a = Matrix([[Complex(1, 2), Complex(2, 3)], [Complex(3, 4), Complex(4, 5)]])
    print(a)
    print(f"Rank = {a.rank()}", end="\n\n")


if __name__ == '__main__':
    main()
