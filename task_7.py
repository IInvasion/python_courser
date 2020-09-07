import sys

def factorial(n):
    """Factorial."""
    result = 1
    for i in range(1, n+1):
        result *= i
        yield result

def _main():
    """Entry point."""
    n = 20
    result = factorial(n)
    for element in result:
        print(element)

if __name__ == '__main__':
    sys.exit(_main())