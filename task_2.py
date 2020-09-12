import sys

def _main():
    """Entry point."""
    with open('task_2.txt', encoding='utf-8') as f_obj:
        lines_number = 0
        for line in f_obj:
            lines_number += 1
            print(f'In {lines_number} string {len(line.split())} words')
        print(f'{lines_number} strings in the file')

if __name__ == '__main__':
    sys.exit(_main())