number = int(input('Enter positive number: '))
div = 1
result = 0
while (number // div) != 0:
    div *= 10
    quot = (number % div) // (div // 10)
    if quot > result:
        result = quot
print(result)