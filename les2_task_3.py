seasons_dikt = {"Winter": (1, 2, 12), "Spring": (3, 4, 5), "Summer": (6, 7, 8), "Autumn": (9, 10, 11)}
number_of_month = int(input('Enter a number of month: '))
for key in seasons_dikt.keys():
    if number_of_month in seasons_dikt[key]:
        print(key)
        break




