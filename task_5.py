import sys
import random


def _main():
    """Entry point."""
    with open('task_5.txt', 'w+', encoding='utf-8') as f_obj:
        result = 0
        for _ in range(100):
            integer = random.randint(0, 100)
            print(integer, end=' ', file=f_obj)
        f_obj.seek(0)
        content = f_obj.read()
        content = content.split()
        for element in content:
            result += int(element)
        print(result)


if __name__ == '__main__':
    sys.exit(_main())