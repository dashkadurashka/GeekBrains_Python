my_list = [5, 4, 3, 2, 2, 45, 13, 47, 8, 5, 20, 20, 20, 3]
new_list = [i for i in my_list if my_list.count(i) < 2]
print(new_list)
