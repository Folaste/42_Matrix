from complex import Complex


class Matrix:

    def __init__(self, *elements) -> None:
        try:
            if not all(isinstance(elem, list) for elem in elements) or len(elements) != 1:
                raise AssertionError("Constructor takes only 1 list.")
            elements = elements[0]

            if not all(isinstance(line, list) for line in elements) or len(elements) == 0:
                raise AssertionError("Matrix must contain lists.")
            else:
                width = len(elements[0])
                for line in elements:
                    if len(line) != width:
                        raise AssertionError("All lists in matrix must have same length.")

            for line in elements:
                if len(line) == 0:
                    raise AssertionError("Lines must contain numbers.")

                if not all(isinstance(elem, (int, float, Complex)) for elem in line):
                    raise AssertionError("Matrix must only contain float, int or complex numbers.")

                if (not all(isinstance(elem, Complex) for elem in line) and
                        not all(isinstance(elem, (int, float)) for elem in line)):
                    raise AssertionError("Only real or complex numbers may be used in the rows of the matrix.")

            test_col = []
            for i in range(len(elements)):
                test_col.append(elements[i][0])

            if (not all(isinstance(elem, (float, int)) for elem in test_col)
                    and not all(isinstance(elem, Complex) for elem in test_col)):
                raise AssertionError("All elements must be in the same type. (Real or Complex numbers)")

            self._elements = elements
            self._rows = len(elements)
            self._columns = len(elements[0])

        except AssertionError as e:
            print(e)
            raise AssertionError("Error while creating Matrix")

    def __str__(self) -> str:
        rows_str = "\n".join(f"[{', '.join(str(elem) for elem in row)}]" for row in self._elements)
        return f"{rows_str}"

    def __repr__(self) -> str:
        return "Matrix({})".format(self._elements)

    def shape(self) -> (int, int):
        return self._rows, self._columns

    def is_square(self) -> bool:
        return self._rows == self._columns

    def to_vector(self):
        from vector import Vector
        return Vector([elem for row in self._elements for elem in row])
