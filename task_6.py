a = float(input("Начальная дистанция:"))
b = float(input("Конечная дистанция:"))
day = 1
while a < b:
    a = a + a * 0.1
    day += 1
print(f"Спортсмен достигнет результата за {day} дней")
