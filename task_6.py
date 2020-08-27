current_result = int(input('Enter first day result: '))
targer_result = int(input('Enter targer result: '))
day = 1
while current_result < targer_result:
    current_result *= 1.1
    day += 1
print(day)
