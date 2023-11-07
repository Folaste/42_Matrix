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

    # ex00
    def __add__(self, other):
        try:
            if not isinstance(other, Matrix):
                raise AssertionError("Matrix can only be add with another matrix.")
            if self._rows != other._rows or self._columns != other._columns:
                raise AssertionError("Matrix must have same shape.")

            result = []
            for i in range(0, self._rows):
                result_line = []
                for j in range(0, self._columns):
                    result_line.append(self._elements[i][j] + other._elements[i][j])
                result.append(result_line)
            return Matrix(result)

        except AssertionError as e:
            print(e)

    def __sub__(self, other):
        try:
            if not isinstance(other, Matrix):
                raise AssertionError("Matrix can only be subtract with another matrix.")
            if self._rows != other._rows or self._columns != other._columns:
                raise AssertionError("Matrix must have same shape.")

            result = []
            for i in range(0, self._rows):
                result_line = []
                for j in range(0, self._columns):
                    result_line.append(self._elements[i][j] - other._elements[i][j])
                result.append(result_line)
            return Matrix(result)

        except AssertionError as e:
            print(e)

    def scl(self, scalar):
        try:
            if not isinstance(scalar, (int, float, Complex)):
                raise AssertionError("Scalar must be a number (Real or Complex)")

            result = []
            for i in range(0, self._rows):
                result_line = []
                for j in range(0, self._columns):
                    result_line.append(self._elements[i][j] * scalar)
                result.append(result_line)
            return Matrix(result)

        except AssertionError as e:
            print(e)
