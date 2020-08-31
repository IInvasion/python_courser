while True:
    list_count = input('Enter list elements number: ')
    if list_count.isdigit():
        break

my_list = []
for i in range(int(list_count)):
    element = input('Enter next element: ')
    my_list.append(element)
print(my_list)
counter = 0
while counter < len(my_list) - 1:
    my_list[counter], my_list[counter+1] = my_list[counter+1], my_list[counter]
    counter += 2
print(my_list)