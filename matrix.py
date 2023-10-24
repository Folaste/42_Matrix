class Matrix:

    def __init__(self, elements):
        try:
            width = len(elements[0])
        except AssertionError as e:
            print(e)
            exit(1)

        self.elements = elements
        self.height = len(elements)
        self.width = len(elements[0])
