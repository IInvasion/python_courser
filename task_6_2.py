import sys
from itertools import cycle

def _main():
    """Entry point."""
    initial_list = [1, 2, 3, 4, 5]
    counter = 0
    for element in cycle(initial_list):
        if counter > 55:
            break
        print(element)
        counter += 1

if __name__ == '__main__':
    sys.exit(_main())