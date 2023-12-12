"""
    Class Matrix using my type complex (Class Complex in directory)
"""

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

            nb_rows = len(elements)
            nb_cols = len(elements[0])

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

            self._repr = elements  # Only used by __repr__()

            self._elements = elements
            self._rows = nb_cols
            self._columns = nb_rows

        except AssertionError as e:
            print(e)
            raise AssertionError("Error while creating Matrix")

    # utils
    def __str__(self) -> str:
        elements = [[self._elements[j][i] for j in range(self._columns)] for i in range(self._rows)]
        rows_str = "\n".join(f"[{', '.join(str(elem) for elem in row)}]" for row in elements)
        return f"{rows_str}\n"

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

    def submatrix(self, i, j):
        """ Returns the sub-matrix without the i-th row and the j-th column. """
        return Matrix([[self._elements[b][a] for a in range(self._columns) if a != i]
                       for b in range(self._rows) if b != j])

    # ex00
    def __add__(self, other):
        # Time complexity: O(n^2)
        # Space complexity: O(n^2)
        try:
            if not isinstance(other, Matrix):
                raise AssertionError("Matrix can only be add with another matrix.")
            if self._rows != other._rows or self._columns != other._columns:
                raise AssertionError("Matrix must have same shape.")

            result = []
            for i in range(0, self._columns):
                result_line = []
                for j in range(0, self._rows):
                    result_line.append(self._elements[i][j] + other._elements[i][j])
                result.append(result_line)
            return Matrix(result)

        except AssertionError as e:
            print(e)

    def __sub__(self, other):
        # Time complexity: O(n^2)
        # Space complexity: O(n^2)
        try:
            if not isinstance(other, Matrix):
                raise AssertionError("Matrix can only be subtract with another matrix.")
            if self._rows != other._rows or self._columns != other._columns:
                raise AssertionError("Matrix must have same shape.")

            result = []
            for i in range(0, self._columns):
                result_line = []
                for j in range(0, self._rows):
                    result_line.append(self._elements[i][j] - other._elements[i][j])
                result.append(result_line)
            return Matrix(result)

        except AssertionError as e:
            print(e)

    def __mul__(self, other):
        from vector import Vector
        try:
            # Time complexity: O(n^2)
            # Space complexity: O(n^2)
            if isinstance(other, (int, float, Complex)):  # ex00
                result = []
                for i in range(0, self._columns):
                    result_line = []
                    for j in range(0, self._rows):
                        result_line.append(self._elements[i][j] * other)
                    result.append(result_line)
                return Matrix(result)

            elif isinstance(other, Vector):  # ex07
                # Time complexity: O(n^2)
                # Space complexity: O(n)
                if self._columns == other.dim():
                    result = []
                    for i in range(self._rows):
                        element = 0
                        for j in range(other.dim()):
                            element += self._elements[j][i] * other[j]
                        result.append(element)
                    return Vector(result)
                else:
                    raise ValueError("The dimension of the vector must be equal "
                                     "to the number of columns in the matrix.")

            elif isinstance(other, Matrix):  # ex07
                # Time complexity: O(n^3)
                # Space complexity: O(n^2)
                if self._columns == other._rows:
                    result = []
                    for j in range(other._columns):
                        result_line = []
                        for i in range(self._rows):
                            element = 0
                            for k in range(self._columns):
                                element += self._elements[k][i] * other._elements[j][k]
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

    # ex08
    def trace(self):
        """ Returns the trace of the matrix. """
        # Time complexity: O(n)
        # Space complexity: O(1)
        try:
            if self.is_square():
                return sum(self._elements[i][i] for i in range(self._rows))
            else:
                raise ValueError("Matrix must be square.")

        except ValueError as e:
            print(e)

    # ex09
    def transpose(self):
        """ Returns the transpose of the matrix. """
        # Time complexity: O(mn)
        # Space complexity: O(mn)
        return Matrix([[self._elements[j][i] for j in range(self._columns)] for i in range(self._rows)])

    # ex10
    def row_echelon(self):
        """ Returns the row echelon form of the matrix. """
        # Time complexity: O(n^3)
        # Space complexity: O(n^2)
        # Apply transpose to the matrix to make it row-major order.
        ref = [[self._elements[j][i] for j in range(self._columns)] for i in range(self._rows)]
        r = 0
        # Step 1: Begin with the first non-zero column. This is the pivot column.
        for j in range(self._columns):
            if not all(ref[i][j] == 0 for i in range(self._rows)):
                # Step 2: Make all entries below the pivot zero by using row operations. This is called the pivot row.
                # If there is no pivot row, then interchange rows to create one.
                i = r
                while i < self._rows and ref[i][j] == 0:
                    i += 1
                if i < self._rows:
                    ref[r], ref[i] = ref[i], ref[r]
                else:
                    continue
                # Step 3: Make all entries in the pivot column zero except for the pivot entry.
                for i in range(self._rows):
                    if ref[i][j] != 0 and i != r:
                        ref[i] = [ref[i][k] - ref[r][k] * ref[i][j] / ref[r][j] for k in range(self._columns)]
                # Step 4: Make the pivot entry one by dividing the pivot row by the pivot entry.
                ref[r] = [ref[r][k] / ref[r][j] for k in range(self._columns)]
                ref[r] = [0. if x == -0. else x for x in ref[r]]
                r += 1
                if r == self._rows:
                    break
            # Step 5: Repeat steps 1 through 4 on the sub-matrix that is below and to the right of the pivot
        # Apply transpose to the matrix to make it column-major order.
        ref = [[ref[j][i] for j in range(self._rows)] for i in range(self._columns)]
        return Matrix(ref)

    # ex11
    def determinant(self):
        from ft_math import ft_pow
        """ Returns the determinant of the matrix."""
        # Time complexity: O(n!)
        # Space complexity: O(n)
        try:
            if self.is_square():
                if self._rows == 1:
                    return self.elements[0][0]
                elif self._rows <= 4:
                    return sum(ft_pow(-1, i) * self.submatrix(i, 0).determinant() * self._elements[0][i]
                               for i in range(self._rows))
                else:
                    raise ValueError("Matrix must be smaller than 5x5.")
            else:
                raise ValueError("Matrix must be square.")

        except ValueError as e:
            print(e)

    # ex12
    def inverse(self):
        """ Returns the inverse of the matrix. """
        # Time complexity: O(n^3)
        # Space complexity: O(n^2)
        from ft_math import ft_pow
        try:
            if self.is_square():
                det = self.determinant()
                if det == 0:
                    raise ValueError("Matrix is not invertible.")
                else:
                    return Matrix([
                        [ft_pow(-1, i + j) * self.submatrix(j, i).determinant()
                         for j in range(self._rows)]
                        for i in range(self._columns)]).transpose() * (1 / self.determinant())
            else:
                raise ValueError("Matrix must be square.")

        except ValueError as e:
            print(e)

    # ex13
    def rank(self):
        """ Returns the rank of the matrix. """
        # Time complexity: O(n^2)
        # Space complexity: O(1)
        ref = self.row_echelon()
        rank = 0
        for i in range(self._rows):
            if not all(ref.elements[j][i] == 0 for j in range(self._columns)):
                rank += 1
        return rank

    @property
    def elements(self):
        return self._elements
