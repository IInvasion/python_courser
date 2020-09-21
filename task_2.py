"""Eight lesson second practice task."""

import sys


class DivisionByZeroError(Exception):
    """Division by zero exception."""

    def __init__(self, text):
        """Constructor."""
        self.text = text


def _main():
    """Entry point."""
    try:
        divident = float(input('Enter divident: '))
        divisor = float(input('Enter divisor: '))
        if divisor == 0:
            raise DivisionByZeroError('Divisor should not be zero')
        result = divident / divisor
        print(f'Result = {result}')
    except ValueError:
        print('Divident and divisor should be a number')
    except DivisionByZeroError as err:
        print(err)
    finally:
        print('Program terminated')


if __name__ == '__main__':
    sys.exit(_main())
