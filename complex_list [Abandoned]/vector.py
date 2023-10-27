class Vector:

    def __init__(self, *elements: list):
        try:
            if not all(isinstance(elem, list) for elem in elements) or len(elements) != 1:
                raise AssertionError("Constructor takes only 1 list.")
            elements = elements[0]

            if not all(isinstance(elem, (int, float, list)) for elem in elements) or len(elements) == 0:
                raise AssertionError("Vector must only contain float, int or complex numbers.")

            if all(isinstance(elem, list) for elem in elements):
                c_elements = []
                for elem in elements:
                    if not all(isinstance(comp, (int, float)) for comp in elem) or len(elem) != 2:
                        raise AssertionError("Complex number must have only 2 parts and must be ints or floats.")
                    elem = [float(comp) for comp in elem]
                    c_elements.append(elem)
                self.elements = c_elements
                self.dimension = len(c_elements)
                self.complex = True

            elif not all(isinstance(elem, (int, float)) for elem in elements):
                raise AssertionError("Vector must only contain float, int or complex numbers.")

            else:
                elements = [float(elem) for elem in elements]
                self.elements = elements
                self.dimension = len(elements)
                self.complex = False

        except AssertionError as e:
            print(e)
            raise AssertionError("Error while creating Vector")

    def dim(self) -> None:
        print(f"Size of the vector is : {self.dimension}")

    def print(self) -> None:
        if self.complex is True:
            print("[", end='')
            for i in range(self.dimension):
                if self.elements[i][1] < 0:
                    print(f"{self.elements[i][0]}{self.elements[i][1]}i", end='')
                else:
                    print(f"{self.elements[i][0]}+{self.elements[i][1]}i", end='')
                if i != self.dimension - 1:
                    print(", ", end='')
            print("]")
        else:
            print(self.elements)
