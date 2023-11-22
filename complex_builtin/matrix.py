"""
    Class Matrix with built-in complex type.
"""


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

            nb_rows = len(elements)
            nb_cols = len(elements[0])

            for line in elements:
                if len(line) == 0:
                    raise AssertionError("Lines must contain numbers.")

                if not all(isinstance(elem, (int, float, complex)) for elem in line):
                    raise AssertionError("Matrix must only contain float, int or complex numbers.")

                if (not all(isinstance(elem, complex) for elem in line) and
                        not all(isinstance(elem, (int, float)) for elem in line)):
                    raise AssertionError("Only real or complex numbers may be used in the rows of the matrix.")

            test_col = []
            for i in range(len(elements)):
                test_col.append(elements[i][0])

            if (not all(isinstance(elem, (float, int)) for elem in test_col)
                    and not all(isinstance(elem, complex) for elem in test_col)):
                raise AssertionError("All elements must be in the same type. (Real or Complex numbers)")

            self._repr = elements  # Only used by __repr__()

            elements = [[elements[j][i] for j in range(nb_rows)] for i in range(nb_cols)]

            self._elements = elements
            self._rows = len(elements)
            self._columns = len(elements[0])

        except AssertionError as e:
            print(e)
            raise AssertionError("Error while creating Matrix")

    def __str__(self) -> str:
        return "{}".format('\n'.join(map(str, self._elements)))

    def __repr__(self) -> str:
        return "Matrix({})".format(self._repr)

    def shape(self) -> (int, int):
        """ Returns size of the matrix. """
        return self._rows, self._columns

    def is_square(self) -> bool:
        """ Returns True if the matrix is square, False otherwise. """
        return self._rows == self._columns

    def to_vector(self):
        """ Create a vector with values of the matrix. """
        from vector import Vector
        return Vector([elem for row in self._elements for elem in row])

    def __add__(self, other):
        try:
            if not isinstance(other, Matrix):
                raise AssertionError("Matrix can only add with another matrix.")
            if self._rows != other._rows or self._columns != other._columns:
                raise AssertionError("Matrix must have same shapes.")

            result = []
            for i in range(0, self._columns):
                result_col = []
                for j in range(0, self._rows):
                    result_col.append(self._elements[j][i] + other._elements[j][i])
                result.append(result_col)
            return Matrix(result)

        except AssertionError as e:
            print(e)

    def __sub__(self, other):
        try:
            if not isinstance(other, Matrix):
                raise AssertionError("Matrix can only subtract with another matrix.")
            if self._rows != other._rows or self._columns != other._columns:
                raise AssertionError("Matrix must have same shape.")

            result = []
            for i in range(0, self._columns):
                result_col = []
                for j in range(0, self._rows):
                    result_col.append(self._elements[j][i] - other._elements[j][i])
                result.append(result_col)
            return Matrix(result)

        except AssertionError as e:
            print(e)

    def __mul__(self, other):
        from complex_builtin.vector import Vector
        try:
            if isinstance(other, (int, float, complex)):  # ex00
                result = []
                for i in range(0, self._columns):
                    result_line = []
                    for j in range(0, self._rows):
                        result_line.append(self._elements[j][i] * other)
                    result.append(result_line)
                return Matrix(result)

            elif isinstance(other, Vector):  # ex07
                if self._columns == other.dim():
                    result = []
                    for i in range(self._rows):
                        element = 0
                        for j in range(other.dim()):
                            element += self._elements[i][j] * other[j]
                        result.append(element)
                    return Vector(result)
                else:
                    raise ValueError("The dimension of the vector must be equal"
                                     " to the number of columns in the matrix.")

            elif isinstance(other, Matrix):  # ex07
                if self._columns == other._rows:
                    result = []
                    for j in range(other._columns):
                        result_line = []
                        for i in range(self._rows):
                            element = 0
                            for k in range(self._columns):
                                element += self._elements[i][k] * other._elements[k][j]
                            result_line.append(element)
                        result.append(result_line)
                    return Matrix(result)
                else:
                    raise ValueError("The number of columns in the first matrix must be equal "
                                     "to the number of rows in the second matrix.")

            else:
                raise AssertionError("Parameter must be a scalar (Real or Complex), a Vector or a Matrix.")

        except ValueError as e:
            print(e)
        except AssertionError as e:
            print(e)

    def __rmul__(self, other):
        return self.__mul__(other)
