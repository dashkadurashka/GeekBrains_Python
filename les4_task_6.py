from itertools import count

num = int(input('Enter start number: '))
for i in count(num):
    if i > num + 5:
        break
    else:
        print(i)

from itertools import cycle

my_list = ['A', 'B', 'C', 'D']
count = 0
for j in cycle(my_list):
    if count > 5:
        break
    print(j)
    count += 1
