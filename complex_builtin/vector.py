"""
    Class Vector with built-in complex type.
"""


from ft_math import ft_sqrt, ft_pow, ft_abs


class Vector:

    def __init__(self, *elements) -> None:
        if not all(isinstance(element, list) for element in elements) or len(elements) != 1:
            raise AssertionError("vector.__init__: Constructor takes only 1 list.")
        elements = elements[0]

        if not all(isinstance(elem, (int, float, complex)) for elem in elements) or len(elements) == 0:
            raise AssertionError("vector.__init__: Vector must only contain float, int or complex numbers.")

        if (all(isinstance(elem, complex) for elem in elements)
                or all(isinstance(elem, (int, float)) for elem in elements)):
            self._elements = elements
            self._dimension = len(elements)
        else:
            raise AssertionError("vector.__init__: All numbers must be in the same types (Real or Complex).")

    # utils
    def __getitem__(self, index):
        try:
            if index < self._dimension:
                return self._elements[index]
            raise AssertionError("vector.__getitem__: Index is above dimension of the vector.")
        except AssertionError as e:
            print(e)

    def __str__(self) -> str:
        max_width = max(len(str(element)) for element in self._elements)
        string = ""
        for elem in self._elements:
            centered_element = str(elem).center(max_width)
            string += "| {:} |\n".format(centered_element)
        return string

    def __repr__(self) -> str:
        return f"Vector({self._elements})"

    def dim(self) -> int:
        """ Returns length of the vector. """
        return self._dimension

    def to_matrix(self, rows, columns):
        """ Create a matrix with values of the vector. """
        from complex_builtin.matrix import Matrix
        if self._dimension != rows * columns:
            raise AssertionError("vector.to_matrix: Matrix shape's product must be equal to vector's dimension")
        return Matrix([self._elements[i:i+rows] for i in range(0, len(self._elements), rows)])

    # ex00
    def __add__(self, other):
        if not isinstance(other, Vector):
            raise AssertionError("vector.__add__: Vector can only be add with another vector.")
        if other._dimension != self._dimension:
            raise AssertionError("vector.__add__: Vectors must have same size.")

        return Vector([self._elements[i] + other._elements[i] for i in range(0, self._dimension)])

    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise AssertionError("vector.__sub__: Vector can only subtract with another vector.")
        if other._dimension != self._dimension:
            raise AssertionError("vector.__sub__: Vector must have same size.")

        return Vector([self._elements[i] - other._elements[i] for i in range(0, self._dimension)])

    def __mul__(self, other):
        if isinstance(other, (int, float, complex)):  # ex00
            return Vector([self._elements[i] * other for i in range(0, self._dimension)])

        elif isinstance(other, Vector):  # ex03
            if self._dimension != other._dimension:
                raise ValueError("vector.__mul__: Vector must have same dimension.")
            result = 0
            for i in range(self._dimension):
                result += self._elements[i] * other._elements[i]
            return result

        else:
            raise AssertionError("vector.__mul__: Parameter must be a scalar number (Real or Complex), or a Vector")

    def __rmul__(self, other):
        if isinstance(other, (int, float, complex)):
            return self.__mul__(other)

    # ex04
    def norm_1(self) -> float:
        """ Returns Manhattan norm for the vector. """
        result = sum([ft_abs(elem, 'manhattan') for elem in self._elements])
        return result

    def norm(self) -> float:
        """ Returns Euclidean norm for the vector. """
        result = sum(ft_pow(elem, 2) for elem in self._elements)
        return ft_sqrt(result)

    def norm_inf(self) -> float:
        """ Returns supremum norm for the vector. """
        val_abs = [ft_abs(elem, 'manhattan') for elem in self._elements]
        return max(val_abs)
