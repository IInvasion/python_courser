while True:
    month_number = input('Enter month number (from 1 to 12): ')
    if month_number.isdigit and int(month_number) in range(1, 13):
        break

seasons = {
            'summer': [6, 7, 8],
            'fall': [9, 10, 11],
            'winter': [1, 2, 12],
            'spring': [3, 4, 5]
          }

for key, value in seasons.items():
    if int(month_number) in value:
        print(key)
        break