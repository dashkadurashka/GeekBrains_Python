my_f = open('text_4.txt', 'r', encoding='utf-8')
line = my_f.readlines()
for i, j in enumerate(line, 1):
    words = len(j   .split())
    print(f"String {i} contains {words} words")
print(f"All strings - {len(line)}")

my_f.close()