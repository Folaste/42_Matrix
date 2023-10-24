class Vector:

    def __init__(self, elements):
        self.elements = elements
        self.size = len(elements)

    def size(self):
        print(f"Size of the vector is : {self.size}")

    def print(self):
        print(self.elements)
        # TODO: Complex case
