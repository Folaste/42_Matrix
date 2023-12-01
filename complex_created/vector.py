"""
    Class Vector using my type complex (Class Complex in directory)
"""


from complex_created.complex import Complex
from ft_math import ft_abs, ft_pow, ft_sqrt


class Vector:

    def __init__(self, *elements) -> None:
        try:
            if not all(isinstance(element, list) for element in elements) or len(elements) != 1:
                raise AssertionError("Constructor takes only 1 list.")
            elements = elements[0]

            if not all(isinstance(elem, (int, float, Complex)) for elem in elements) or len(elements) == 0:
                raise AssertionError("Vector must only contain float, int or complex numbers.")

            if (all(isinstance(elem, Complex) for elem in elements)
                    or all(isinstance(elem, (int, float)) for elem in elements)):
                self._elements = elements
                self._dimension = len(elements)
            else:
                raise AssertionError("All numbers must be in the same types (Real or Complex).")

        except AssertionError as e:
            print(e)
            raise AssertionError("Error while creating Vector")

    # utils
    def __getitem__(self, index):
        try:
            if index < self._dimension:
                return self._elements[index]
            raise AssertionError("Index is above dimension of the vector.")
        except AssertionError as e:
            print(e)

    def __str__(self):
        max_width = max(len(str(element)) for element in self._elements)
        string = ""
        for elem in self._elements:
            centered_element = str(elem).center(max_width)
            string += "| {:} |\n".format(centered_element)
        return string

    def __repr__(self):
        elements_repr = ", ".join(repr(element) for element in self._elements)
        return f"Vector([{elements_repr}])"

    def dim(self) -> int:
        """ Returns length of the vector. """
        return self._dimension

    def to_matrix(self, rows, columns):
        """ Create a matrix with values of the vector. """
        from matrix import Matrix
        try:
            if self._dimension != rows * columns:
                raise AssertionError("Matrix shape's product must be equal to vector's dimension")
            return Matrix([self._elements[i:i+rows] for i in range(0, len(self._elements), rows)])
        except AssertionError as e:
            print(e)

    # ex00
    def __add__(self, other):
        try:
            if not isinstance(other, Vector):
                raise AssertionError("Vector can only be add with another vector.")
            if self._dimension != other._dimension:
                raise AssertionError("Vectors must have same size.")

            return Vector([self._elements[i] + other._elements[i] for i in range(0, self._dimension)])

        except AssertionError as e:
            print(e)

    def __sub__(self, other):
        try:
            if not isinstance(other, Vector):
                raise AssertionError("Vector can only be subtract with another vector.")
            if self._dimension != other._dimension:
                raise AssertionError("Vector must have same size.")

            return Vector([self._elements[i] - other._elements[i] for i in range(0, self._dimension)])

        except AssertionError as e:
            print(e)

    def __mul__(self, other):
        try:
            if isinstance(other, (int, float, Complex)):  # ex00
                return Vector([self._elements[i] * other for i in range(0, self._dimension)])

            elif isinstance(other, Vector):  # ex03
                if self._dimension != other._dimension:
                    raise ValueError("Vector must have same dimension.")
                result = 0
                for i in range(self._dimension):
                    result += self._elements[i] * other._elements[i]
                return result

            else:
                raise AssertionError("Parameter must be a scalar number (Real or Complex), or a Vector")

        except AssertionError as e:
            print(e)
        except ValueError as e:
            print(e)

    def __rmul__(self, other):
        return self.__mul__(other)

    # ex04
    def norm_1(self) -> float:
        """ Returns Manhattan norm for the vector. """
        try:
            result = sum([ft_abs(elem, 'manhattan') for elem in self._elements])
            return float(result)

        except AssertionError as e:
            print(e)

    def norm(self) -> float:
        """ Returns Euclidean norm for the vector. """
        try:
            result = sum(ft_pow(ft_abs(elem), 2) for elem in self._elements)
            return ft_sqrt(result)

        except AssertionError as e:
            print(e)

    def norm_inf(self) -> float:
        """ Returns supremum norm for the vector. """
        try:
            val_abs = [ft_abs(elem, 'manhattan') for elem in self._elements]
            return float(max(val_abs))

        except AssertionError as e:
            print(e)
