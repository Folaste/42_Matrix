class Matrix:

    def __init__(self, *elements):
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
                        raise AssertionError("All list in matrix must same length.")

            matrix = []

            for line in elements:
                if len(line) == 0:
                    raise AssertionError("Lines must contain numbers.")

                if not all(isinstance(elem, (int, float, list)) for elem in line):
                    raise AssertionError("Matrix must only contain float, int or complex numbers.")

                if all(isinstance(elem, list) for elem in line):
                    c_line = []
                    for elem in line:
                        if not all(isinstance(comp, (int, float)) for comp in elem) or len(elem) != 2:
                            raise AssertionError("Complex number must have only 2 parts and must be ints or floats.")
                        elem = [float(comp) for comp in elem]
                        c_line.append(elem)
                    matrix.append(c_line)
                elif not all(isinstance(elem, (int, float)) for elem in line):
                    raise AssertionError("Vector must only contain float, int or complex numbers.")
                else:
                    elem = [float(elem) for elem in line]
                    matrix.append(elem)

            test_col = []
            for i in range(len(matrix)):
                test_col.append(matrix[i][0])

            print(test_col)
            if (not all(isinstance(elem, float) for elem in test_col)
                    and not all(isinstance(elem, list) for elem in test_col)):
                raise AssertionError("All elements must be in the same type.")

            self.elements = matrix
            self.rows = len(matrix)
            self.columns = len(matrix[0])
            if isinstance(matrix[0][0], list):
                self.complex = True
            else:
                self.complex = False

        except AssertionError as e:
            print(e)
            raise AssertionError("Error while creating Matrix")

    def shape(self) -> None:
        print(f"Shape of the matrix is: {self.rows} * {self.columns}")

    def is_square(self) -> bool:
        if self.columns == self.rows:
            return True
        else:
            return False
