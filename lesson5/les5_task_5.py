from random import randint

my_f = open('text_5.txt', mode="w+", encoding="utf-8")
my_f.write(" ".join([str(randint(1, 10)) for _ in range(100)]))
my_f.seek(0)
print(sum(map(int, my_f.readline().split())))
my_f.close()