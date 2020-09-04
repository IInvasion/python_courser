def int_func(word):
    """Title word."""
    return word.title()

word = input('Enter word: ')
new_word = ''
for i in range(len(word)):
    if i == 0:
        if ord(word[i]) >= 97 and ord(word[i]) <= 122:
            new_word += chr(ord(word[i]) - 32)
        else:
            new_word += word[i]
    else:
        new_word += word[i]
print(new_word)
string = input('Enter string of words divided by spaces: ')
new_string = ''
for i in range(len(string)):
    if i == 0 or string[i-1] == ' ':
        if ord(string[i]) >= 97 and ord(string[i]) <= 122:
            new_string += chr(ord(string[i]) - 32)
        else:
            new_string += string[i]
    else:
        new_string += string[i]
print(new_string)
