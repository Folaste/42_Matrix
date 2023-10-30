class Vector:

    def __init__(self, *elements) -> None:
        try:
            if not all(isinstance(element, list) for element in elements) or len(elements) != 1:
                raise AssertionError("Constructor takes only 1 list.")
            elements = elements[0]

            if not all(isinstance(elem, (int, float, complex)) for elem in elements) or len(elements) == 0:
                raise AssertionError("Vector must only contain float, int or complex numbers.")

            if (all(isinstance(elem, complex) for elem in elements)
                    or all(isinstance(elem, (int, float)) for elem in elements)):
                self._elements = elements
                self._dimension = len(elements)
            else:
                raise AssertionError("All numbers must be in the same types (Real or Complex).")

        except AssertionError as e:
            print(e)
            raise AssertionError("Error while creating Vector")

    def __str__(self) -> str:
        return f"{self._elements}"

    def __repr__(self) -> str:
        return f"Vector({self._elements})"

    def dim(self) -> int:
        return self._dimension

    def to_matrix(self, rows, columns):
        from matrix import Matrix
        try:
            if self._dimension != rows * columns:
                raise AssertionError("Matrix shape's product must be equal to vector's dimension")
            return Matrix([self._elements[i:i+columns] for i in range(0, len(self._elements), columns)])
        except AssertionError as e:
            print(e)

    # ex00
    def __add__(self, other):
        try:
            if not isinstance(other, Vector):
                raise AssertionError("Vector can only be add with another vector.")
            if other._dimension != self._dimension:
                raise AssertionError("Vectors must have same size.")

            return Vector([self._elements[i] + other._elements[i] for i in range(0, self._dimension)])

        except AssertionError as e:
            print(e)

    def __sub__(self, other):
        try:
            if not isinstance(other, Vector):
                raise AssertionError("Vector can only subtract with another vector.")
            if other._dimension != self._dimension:
                raise AssertionError("Vector must have same size.")

            return Vector([self._elements[i] - other._elements[i] for i in range(0, self._dimension)])

        except AssertionError as e:
            print(e)

    def scl(self, scalar):
        try:
            if not isinstance(scalar, (int, float, complex)):
                raise AssertionError("Vector must be multiply by a number (Real or Complex)")

            return Vector([self._elements[i] * scalar for i in range(0, self._dimension)])

        except AssertionError as e:
            print(e)
