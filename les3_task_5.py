def my_sum():
    summa = 0
    while True:
        err = False
        my_list = input('Введите несколько чисел (для выхода введите q или Q): ').split()
        for i in my_list:
            if i == 'q' or i == 'Q':
                return summa
            else:
                try:
                    summa = summa + int(i)
                except ValueError:
                    err = True
        if err:
            print('Некорректные данные!')
        print(f"Сумма равна - {summa}")

print(my_sum())
