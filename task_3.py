import sys

def _main():
    """Entry point."""
    result = [element for element in range(20, 241) if element % 20 == 0 or element % 21 == 0]
    print(result)

if __name__ == '__main__':
    sys.exit(_main())