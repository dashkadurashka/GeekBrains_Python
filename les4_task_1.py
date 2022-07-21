from sys import argv

_, hour, price, bonus = argv

print(f'Your salary: {int(hour) * int(price) + int(bonus)}')
