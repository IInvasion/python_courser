import sys
import functools


def string_concatenation(str_1, str_2):
    """Concatenate two strings."""
    return str_1 + ' ' + str_2
    

def _main():
    """Entry point."""
    with open('text_4.txt', encoding='utf-8') as f_obj:
        with open('new_file.txt', 'w', encoding='utf-8') as new_file:
            for line in f_obj:
                processed_line = line.split()
                for i in range(len(processed_line)):
                    if processed_line[i] == 'One':
                        processed_line[i] = 'Один'
                    elif processed_line[i] == 'Two':
                        processed_line[i] = 'Два'
                    elif processed_line[i] == 'Three':
                        processed_line[i] = 'Три'
                    elif processed_line[i] == 'Four':
                        processed_line[i] = 'Четыре'
                print(functools.reduce(string_concatenation, [element for element in processed_line]), file=new_file)


if __name__ == '__main__':
    sys.exit(_main())