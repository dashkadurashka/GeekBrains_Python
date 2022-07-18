def my_func(arg_1, arg_2):
    """Возвращает частное от деления

    Позиционные аргументы:
    arg_1 -- запрашивается у пользователя
    arg_2 -- запрашивается у пользователя

    """
    try:
        arg_1, arg_2 = int(arg_1), int(arg_2)
        result_div = arg_1 / arg_2
    except (ZeroDivisionError, ValueError) as err:
        return err
    return result_div

result_func = my_func(input('Введите делимое: '), input('Введите делитель: '))
print(f'Результат - {result_func:.4}')





