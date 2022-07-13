list_from_string = input('Enter your string: ').split()
print(list_from_string)

for i, j in enumerate(list_from_string, 1):
    print(f'{i} it\'s {j:.10}')