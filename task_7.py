"""Eight lesson seventh practice tasks."""

import sys


class Complex:
    """Complex number."""

    def __init__(self, real_number, imaginary_unit):
        """Constructor."""
        self._real_number = real_number
        self._imaginary_unit = imaginary_unit

    def __add__(self, other):
        """Addition of two complex numbers."""
        return Complex(self._real_number + other._real_number, self._imaginary_unit + other._imaginary_unit)

    def __mul__(self, other):
        """Multiplication of two complex numbers."""
        real_number = self._real_number * other._real_number - self._imaginary_unit * other._imaginary_unit
        imaginary_unit = self._real_number * other._imaginary_unit + other._real_number * self._imaginary_unit
        return Complex(real_number, imaginary_unit)

    def __str__(self):
        """Cast to string."""
        if self._imaginary_unit == 1:
            result = f'{self._real_number}+i'
        elif self._imaginary_unit < 0:
            result = f'{self._real_number}{self._imaginary_unit}i'
        else:
            result = f'{self._real_number}+{self._imaginary_unit}i'

        return result


def _main():
    """Entry point."""
    first_complex = Complex(3, 1)
    print(first_complex)
    second_complex = Complex(2, -3)
    print(second_complex)
    print(first_complex + second_complex)
    print(first_complex * second_complex)


if __name__ == '__main__':
    sys.exit(_main())
