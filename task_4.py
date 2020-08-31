phrase = input('Enter phrase: ')
words = phrase.split()
for word in words:
    print(words.index(word) + 1, word[0:10])
