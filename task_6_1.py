import sys
from itertools import count

def _main():
    """Entry point."""
    for element in count(3):
        if element > 10:
            break
        else:
            print(element)

if __name__ == '__main__':
    sys.exit(_main())