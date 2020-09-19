"""First practice task from seventh lesson."""

import sys


class Matrix:
    """Matrix."""

    def __init__(self, lists):
        """Constructor."""
        self.rows = list()
        for element in lists:
            self.rows.append(element)

    def __str__(self):
        """Cast to string."""
        result = ''
        for row in self.rows:
            for element in row:
                result += f'{element:4}'
            result += '\n'
        return result

    def __add__(self, other):
        """Matrix addition."""
        new_matrix = list()
        try:
            for i in range(max(len(self.rows), len(other.rows))):
                new_row = list()
                for j in range(max(len(self.rows[i]), len(other.rows[i]))):
                    new_row.append(self.rows[i][j] + other.rows[i][j])
                new_matrix.append(new_row)
            new_matrix = Matrix(new_matrix)
            return new_matrix
        except IndexError:
            print('Matrixes should have equal number of rows and cols')


def _main():
    """Entry point."""
    matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    another_matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(matrix)
    print(another_matrix)
    print(matrix + another_matrix)


if __name__ == '__main__':
    sys.exit(_main())
