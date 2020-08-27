earns = int(input('Enter amount of earnings: '))
costs = int(input('Enter amount of costs: '))
finres = earns - costs
if finres > 0:
    print('Earnings is higher than costs')
    print(f'Profitability = {(finres / earns):2}')
    employees = int(input('Enter number of company employees: '))
    print(f'Finres per one employee is {(finres / employees):2}')
else:
    print('Earning is not higher than costs')
    