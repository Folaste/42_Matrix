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

            matrix = []

            for line in elements:
                if len(line) == 0:
                    raise AssertionError("Lines must contain numbers.")

                if not all(isinstance(elem, (int, float, complex)) for elem in line):
                    raise AssertionError("Matrix must only contain float, int or complex numbers.")

                if all(isinstance(elem, complex) for elem in line) or all(isinstance(elem, (int, float)) for elem in line):
                    matrix.append(line)
                else:
                    raise AssertionError("Only real or complex numbers may be used in the rows of the matrix.")

            test_col = []
            for i in range(len(matrix)):
                test_col.append(matrix[i][0])

            if (not all(isinstance(elem, (float, int)) for elem in test_col)
                    and not all(isinstance(elem, complex) for elem in test_col)):
                raise AssertionError("All elements must be in the same type. (Real or Complex numbers)")

            self._elements = matrix
            self._rows = len(matrix)
            self._columns = len(matrix[0])

        except AssertionError as e:
            print(e)
            raise AssertionError("Error while creating Matrix")

    def __str__(self) -> str:
        return "{}".format('\n'.join(map(str, self._elements)))

    def __repr__(self) -> str:
        return "Matrix({})".format(self._elements)