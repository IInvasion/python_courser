def division(a, b):
    """Division of two numbers."""
    try:
        result = a / b
        return round(result)
    except ZeroDivisionError:
        print('Division by zero is impossible!')

while True:
    dividend = input('Enter first number: ')
    if dividend.isdigit():
        dividend = float(dividend)
        break
while True:
    divider = input('Enter second number: ')
    if divider.isdigit():
        divider = float(divider)
        break
result = division(dividend, divider)
if result:
    print(result)