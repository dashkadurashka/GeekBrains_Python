season_list = ['Winter', 'Winter', 'Spring', 'Spring', 'Spring', 'Summer', 'Summer', 'Summer', 'Autumn', 'Autumn', 'Autumn', 'Winter']
number_of_month = int(input('Enter a number of month: '))

if 1 <= number_of_month <= 12:
    print(f'{season_list[number_of_month - 1]}')
else:
    print('Err')