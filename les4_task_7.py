from math import factorial


def fact(n):
    for i in range(1, n + 1):
        yield i


for j in fact(int(input('Enter number: '))):
    print(factorial(j))
