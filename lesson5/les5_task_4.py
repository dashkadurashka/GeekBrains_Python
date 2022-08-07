rus_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open("new_text_4.txt", "w", encoding="utf-8") as my_f:
    with open("text_4.txt", encoding="utf-8") as my_new_f:
        my_f.writelines([line.replace(line.split()[0], rus_dict.get(line.split()[0])) for line in my_new_f])
