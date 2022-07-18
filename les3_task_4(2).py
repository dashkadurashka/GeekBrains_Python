def pow_func(x, y):
    if x <= 0 or y >= 0:
        return 'Некорректные данные'
    else:
        result = 1
        for i in range(abs(y)):
            result = result * (1 / x)
        return result

print(pow_func(float(input('Введите действительное положительное число: ')),
             int(input('Введите целое отрицательнео число: '))))