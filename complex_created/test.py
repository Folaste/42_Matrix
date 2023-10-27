from complex import Complex


def main():
    c = Complex(2, 9)
    print(c)
    repr_c = repr(c)
    new_c = eval(repr_c)
    print(new_c)


if __name__ == "__main__":
    main()
