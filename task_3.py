"""Eight lesson third practice task."""

import sys


class NotNumberError(Exception):
    """String is not number error."""

    def __init__(self, text):
        """Constructor."""
        self.text = text


def _main():
    """Entry point."""
    result = list()
    while True:
        try:
            element = input('Enter a number or q for quit: ')
            if element == 'q':
                break
            if not element.isdigit():
                raise NotNumberError('List element should be an integer')
            result.append(int(element))
        except NotNumberError as err:
            print(err)
    print(result)


if __name__ == '__main__':
    sys.exit(_main())
