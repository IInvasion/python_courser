import sys


def _main():
    """Entry point."""
    classes = dict()
    with open('text_6.txt', encoding='utf-8') as f_obj:
        for line in f_obj:
            discipline = line.split()
            discipline_name = discipline[0][:-1]
            hours = 0
            for i in range(1, 4):
                if discipline[i] != '-':
                    hours += int(discipline[i].split('(')[0])
            classes.update({discipline_name: hours})
    print(classes)

if __name__ == '__main__':
    sys.exit(_main())