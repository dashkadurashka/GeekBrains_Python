my_list = [7, 5, 3, 3, 2]
new_number = int(input("Введите цифру от 1 до 9: "))
n = my_list.count(new_number)
for i in my_list:
    if n > 0:
        i = my_list.index(new_number)
        my_list.insert(i + n, new_number)
        break
    else:
        if new_number > i:
            k = my_list.index(i)
            my_list.insert(k, new_number)
            break
        elif new_number < my_list[len(my_list) - 1]:
            my_list.append(new_number)
print(my_list)




