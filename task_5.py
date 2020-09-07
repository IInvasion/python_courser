import sys
from functools import reduce

def summ(a, b):
    """Summ of two neighbour elements."""
    return a + b

def _main():
    """Entry point."""
    result = reduce(summ, [element for element in range(100, 1001) if element % 2 ==0])
    print(result)

if __name__ == '__main__':
    sys.exit(_main())