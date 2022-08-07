my_f = open('text_3.txt', 'r', encoding='utf-8')
my_dict = {line.split()[0]: float(line.split()[1]) for line in my_f}
print(f"Средняя зарплата = {sum(my_dict.values()) / len(my_dict)}")
print(f"Зарплата меньше 20000 у следующих сотрудников: {[i[0] for i in my_dict.items() if i[1] < 20000]}")
my_f.close()