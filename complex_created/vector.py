from complex import Complex


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

    def __str__(self):
        elements_str = ", ".join(str(element) for element in self._elements)
        return f"[{elements_str}]"

    def __repr__(self):
        elements_repr = ", ".join(repr(element) for element in self._elements)
        return f"Vector([{elements_repr}])"

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