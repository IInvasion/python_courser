import sys

def _main():
    """Entry point."""
    try:
        hours = float(sys.argv[1])
        per_hour = float(sys.argv[2])
        bonus = float(sys.argv[3])
        result = (hours * per_hour) + bonus
        print(round(result))
    except ValueError:
        print('Cannot transform string to number')

if __name__ == '__main__':
    sys.exit(_main())