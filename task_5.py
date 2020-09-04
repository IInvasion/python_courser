def process_input(elements):
    """Evaluate sum of integers in string."""
    result = 0
    for element in elements:
        if element.isdigit():
            result += int(element)
    return result


result = 0
while True:
    string = input('Enter string with number divided with spaces (contains q for quit): ')
    elements = string.split()
    summ = process_input(elements)
    result += summ
    print(summ, f'({result})')
    if 'q' in elements:
        break