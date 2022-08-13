my_f = open('text_Dasha.txt', 'w', encoding='utf-8')
text = ' '
while text != '':
    text = input('Enter your text: ')
    print(text, file=my_f)
my_f.close()