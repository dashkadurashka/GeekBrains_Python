def int_func():
    for i in input('Введите слово маленькими латинскими буквами: ').split():
        chars = 0
        for char in i:
            if 97 <= ord(char) <= 122:
                chars += 1
        if chars == len(i):
            print(i.title())
        else:
            print(f"{i} - это не латинские буквы")

int_func()