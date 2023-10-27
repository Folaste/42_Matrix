class Complex:

    def __init__(self, *numbers) -> None:
        try:
            if not all(isinstance(component, (int, float)) for component in numbers) and len(numbers) != 2:
                raise AssertionError("Components must be int or float")

            self._real = numbers[0]
            self._imaginary = numbers[1]

        except AssertionError as e:
            print(e)
            raise AssertionError("Error while creating Complex")

    def __str__(self) -> str:
        return f"{self._real} {('+', '-')[self._imaginary < 0]} {(1, -1)[self._imaginary < 0] * self._imaginary}i"

    def __repr__(self) -> str:
        return f"Complex({self._real}, {self._imaginary})"
