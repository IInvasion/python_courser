def my_func(x, y):
    """Negative power."""
    return x ** y

def another_func(x, y):
    """Negative power."""
    y = abs(y)
    result = 1
    while y > 0:
        result /= x
        y -= 1
    return result

real_number = input('Enter positive real number: ')
try:
    real_number = float(real_number)
    while True:
        power = input('Enter negative integer power: ')
        if power[0] == '-' and power[1:].isdigit():
            power = int(power)
            print(my_func(real_number, power))
            print(another_func(real_number, power))
            break
except:
    print('You should entered real number')