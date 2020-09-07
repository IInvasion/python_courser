import sys

def _main():
    """Entry point."""
    initial_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
    result_list = [initial_list[i] for i in range(1, len(initial_list)) if initial_list[i-1] < initial_list[i]]
    print(result_list)

if __name__ == '__main__':
    sys.exit(_main())