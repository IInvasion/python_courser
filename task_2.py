"""Second practice task for sixth lesson."""

import sys


class Road:
    """Road."""

    def __init__(self, lenght, width):
        """Constructor."""
        self._lenght = lenght
        self._width = width

    def evaluate_covering_mass(self):
        """Evaluate mass of covering road area."""
        return self._lenght * self._width * 25 * 5 / 1000


def _main():
    """Entry point."""
    road = Road(20, 5000)
    print(f'Required {round(road.evaluate_covering_mass(), 3)} ' + \
            'tonnes of material to cover your road')

if __name__ == '__main__':
    sys.exit(_main())
