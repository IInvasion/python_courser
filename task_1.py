import sys

def _main():
    """Entry point."""
    with open('task_1.txt', 'a') as f_obj:
        while True:
            line = input('Enter new line: ')
            if line == '':
                break
            print(line, file=f_obj)

if __name__ == '__main__':
    sys.exit(_main())