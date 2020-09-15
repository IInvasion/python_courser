"""Fifth practice task for sixth lesson."""

import sys


class Stationery:
    """Stationery."""

    def __init__(self, title):
        """Constructor."""
        self._title = title

    def draw(self):
        """Draw."""
        print('Start draw')

    def get_title(self):
        """Get title."""
        return self._title


class Pen(Stationery):
    """Pen."""

    def draw(self):
        """Draw by pen."""
        print('Start draw using pen')


class Pencil(Stationery):
    """Pencil."""

    def draw(self):
        """Draw by pencil."""
        print('Start draw using pencil')


class Handle(Stationery):
    """Handle."""

    def draw(self):
        """Draw by handle."""
        print('Start draw using handle')


def _main():
    """Entry point."""
    stationery = Stationery('Abstract stationery in vacuum')
    pen = Pen('Super cool pen')
    pencil = Pencil('Simple pencil')
    handle = Handle('White board handle')
    print(stationery.get_title())
    print(pen.get_title())
    print(pencil.get_title())
    print(handle.get_title())
    stationery.draw()
    pen.draw()
    pencil.draw()
    handle.draw()


if __name__ == '__main__':
    sys.exit(_main())
