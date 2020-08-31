products = list()
while True:
    products_number = input('Enter products amount: ')
    if products_number.isdigit():
        break
count = 1
for i in range(int(products_number)):
    print('-'*50)
    print('Entering a new product info')
    print('-'*50)
    name = input('Enter product name: ')
    while True:
        cost = input('Enter product cost: ')
        if cost.isdigit():
            break
    while(True):
        number = input('Enter product amount: ')
        if number.isdigit():
            break
    units = input('Enter unit: ')
    product = dict(name=name, cost=int(cost), amount=int(number), units=units)
    products.append((count, product))
    count += 1
analitics = dict(name=[], cost=[], amount=[], units=[])
for product in products:
    for key, value in product[1].items():
        if value not in analitics[key]:
            analitics[key].append(value)
print(analitics)