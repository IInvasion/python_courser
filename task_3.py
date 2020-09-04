def my_func(a, b, c):
    """Sum of max two elements."""
    return sum([a, b, c]) - min(a, b, c)

first = 15
second = 25
third = 50
print(my_func(first, second, third))
