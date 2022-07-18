def func_sum(arg_1, arg_2, arg_3):
    """Возвращает сумму наибольших двух аргументов

    Позиционные аргументы:
    arg_1: запрашивается у пользователя
    arg_2: запрашивается у пользователя
    arg_3: запрашивается у пользователя

    """
    all_arg_in_list = list(map(int, [arg_1, arg_2, arg_3]))
    all_arg_in_list.remove(min(all_arg_in_list))
    return sum(all_arg_in_list)

print(f"Result - {func_sum(int(input('1st arg: ')), int(input('2st arg: ')), int(input('3st arg: ')))}")

