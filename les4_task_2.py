my_list = [17, 20, 9, 17, 1, 8, 3, 6, 15, 4, 89, 5000]
new_list = [i for num, i in enumerate(my_list) if my_list[num - 1] < my_list[num]]
print(new_list)
