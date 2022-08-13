my_dict = {}
numbers = '0123456789 '
my_f = open("text_6.txt", encoding="utf-8")
for i in my_f:
    subj, hours = i.split(":")
    my_dict[subj] = sum(map(int, "".join([num for num in hours if num in numbers]).split()))
print(my_dict)
my_f.close()