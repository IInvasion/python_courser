import sys

def _main():
    """Entry point."""
    initial_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
    result_list = [element for element in initial_list if initial_list.count(element) == 1]
    print(result_list)

if __name__ == '__main__':
    sys.exit(_main())