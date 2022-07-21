from functools import reduce

my_list = [i for i in range(100, 1001) if i % 2 == 0]


def new_func(prev_arg, arg):
    return prev_arg * arg


print(reduce(new_func, my_list))
