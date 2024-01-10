"""
    Complex class using to re-create complex type.
"""


class Complex:

    def __init__(self, *numbers) -> None:
        if not all(isinstance(component, (int, float)) for component in numbers):
            raise AssertionError("Complex.__init__: Components must be int or float.")
        if not len(numbers) == 2:
            raise AssertionError("Complex.__init__: Constructor needs only 2 elements.")

        self._real = numbers[0]
        self._imaginary = numbers[1]

    def __str__(self) -> str:
        sign = "+" if self._imaginary >= 0 else "-"
        return f"{self._real} {sign} {abs(self._imaginary)}i"

    def __repr__(self) -> str:
        return f"Complex({self._real}, {self._imaginary})"

    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self._real + other._real, self._imaginary + other._imaginary)
        elif isinstance(other, (int, float)):
            return Complex(self._real + other, self._imaginary)

    def __iadd__(self, other):
        if isinstance(other, Complex):
            self._real += other._real
            self._imaginary += other._imaginary
        elif isinstance(other, (int, float)):
            self._real += other
        return self

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Complex):
            return Complex(self._real - other._real, self._imaginary - other._imaginary)
        elif isinstance(other, (int, float)):
            return Complex(self._real - other, self._imaginary)

    def __isub__(self, other):
        if isinstance(other, Complex):
            self._real -= other._real
            self._imaginary -= other._imaginary
        elif isinstance(other, (int, float)):
            self._real -= other
        return self

    def __rsub__(self, other):
        return self.__add__(-1 * other)

    def __mul__(self, other):
        if isinstance(other, Complex):
            return Complex(self._real * other._real - self._imaginary * other._imaginary,
                           self._real * other._imaginary + self._imaginary * other._real)
        elif isinstance(other, (int, float)):
            return Complex(self._real * other, self._imaginary * other)

    def __imul__(self, other):
        if isinstance(other, Complex):
            self._real = self._real * other._real - self._imaginary * other._imaginary
            self._imaginary = self._real * other._imaginary + self._imaginary * other._real
        elif isinstance(other, (int, float)):
            self._real *= other
            self._imaginary *= other
        return self

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, Complex):
            return Complex((self._real * other._real + self._imaginary * other._imaginary) / (
                    other._real * other._real + other._imaginary * other._imaginary),
                           (other._real * self._imaginary - self._real * other._imaginary) / (
                                   other._real * other._real + other._imaginary * other._imaginary))
        elif isinstance(other, (int, float)):
            return Complex(self._real / other, self._imaginary / other)

    def __rtruediv__(self, other):
        if isinstance(other, Complex):
            return other.__truediv__(self)
        elif isinstance(other, (int, float)):
            other = Complex(other, 0)
            return other.__truediv__(self)

    @property
    def imaginary(self):
        return self._imaginary

    @property
    def real(self):
        return self._real
