seconds = int(input('Enter seconds: '))
minutes = seconds // 60
seconds = seconds % 60
hours = minutes // 60
minutes = minutes % 60
print(f'Time is {hours}:{minutes}:{seconds}')