import sys

def _main():
    """Entry point."""
    try:
        with open('text_3.txt', encoding='utf-8') as f_obj:
            employees = list()
            for line in f_obj:
                split_line = line.split()
                employee = dict(last_name=split_line[0], salary=float(split_line[1]))
                employees.append(employee)
    except:
        print('Something went wrong')
    summ = 0
    for employee in employees:
        summ += employee['salary']
        if employee['salary'] < 20000:
            print(f'{employee["last_name"]} has salary less then 20000')
    print(f'Average salary equals {summ / len(employees)}')


if __name__ == '__main__':
    sys.exit(_main())