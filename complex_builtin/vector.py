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