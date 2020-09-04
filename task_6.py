def int_func(string):
    """Title words."""
    new_string = ''
    for i in range(len(string)):
        if i == 0 or string[i-1] == ' ':
            if ord(string[i]) >= 97 and ord(string[i]) <= 122:
                new_string += chr(ord(string[i]) - 32)
            else:
                new_string += string[i]
        else:
            new_string += string[i]
    return new_string

word = input('Enter word: ')
print(int_func(word))
string = input('Enter string: ')
print(int_func(string))
