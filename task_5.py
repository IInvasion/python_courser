rating = [7, 5, 3, 3, 2]
print(rating)
while True:
    element = input('Enter rating new element or q for quit: ')
    if element.isdigit():
        for i in range(len(rating)):
            if int(element) > rating[i]:
                rating.insert(i, int(element))
                print(rating)
                break
    elif element == 'q':
        break
