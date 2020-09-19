"""Third practice task from seventh lesson."""

import sys


class Cell:
    """Orgranic cell."""

    def __init__(self, cell_number):
        """Constructor."""
        self.cell_number = cell_number

    def __add__(self, other):
        """Addition of two cells."""
        return Cell(self.cell_number + other.cell_number)

    def __sub__(self, other):
        """Substraction of two cells."""
        return Cell(self.cell_number - other.cell_number if self.cell_number > other.cell_number else print('Substraction is less then zero'))

    def __mul__(self, other):
        """Multiplication of two cells."""
        return Cell(self.cell_number * other.cell_number)

    def __floordiv__(self, other):
        """Floor division of two cells."""
        return Cell(round(self.cell_number / other.cell_number))

    def make_order(self, row):
        """Beautify cells."""
        string = ''
        if row < 1:
            print('Wrong input. Should be greater than zero')
        else:
            for i in range(self.cell_number):
                if (i+1) % row == 0:
                    string += '\n'
                else:
                    string += '*'

        return string


def _main():
    """Entry point."""
    cell_1 = Cell(15)
    cell_2 = Cell(5)
    print('First cell')
    print(cell_1.make_order(4))
    print('Second cell')
    print(cell_2.make_order(4))
    print('Sum of two cells')
    print((cell_1 + cell_2).make_order(4))
    print('Substraction of two cells')
    print((cell_1 - cell_2).make_order(4))
    print('Multiplication of two cells')
    print((cell_1 * cell_2).make_order(14))
    print('Division of two cells')
    print((cell_1 // cell_2).make_order(4))


if __name__ == '__main__':
    sys.exit(_main())
