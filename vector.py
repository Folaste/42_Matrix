class Vector:

    def __init__(self, *elements):
        if not all(isinstance(elem, list) for elem in elements) or len(elements) != 1:
            raise AssertionError("Constructor takes only 1 list.")

        # TODO: Didn't work on complex
        elements = elements[0]
        try:
            if not all(isinstance(elem, (int, float, list))
                       for elem in elements):
                raise AssertionError("Vector must only contain float, "
                                     "int or complex numbers.")
            if all(isinstance(elem, list) for elem in elements):
                for elem in elements:
                    if not all(isinstance(comp, (int, float)) for comp in elem) or len(elem) != 2:
                        raise AssertionError("Complex number must have only 2 "
                                             "parts and must be ints "
                                             "or floats.")
            elif not all(isinstance(elem, (int, float)) for elem in elements):
                raise AssertionError("Vector must only contain float, "
                                     "int or complex numbers.")
            else: # TODO : Tout mettre en float
                self.elements = elements
                print(self.elements)
                self.dimension = len(elements)
        except AssertionError as e:
            print(e)
            exit(1)

    def dim(self):
        print(f"Size of the vector is : {self.dimension}")

    def print(self):
        print(self.elements)
        # TODO: Complex case
