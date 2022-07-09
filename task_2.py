time = int(input('Enter time in seconds:'))

hours = time // 3600
minutes = time % 3600 // 60
seconds = time % 60
print(f'{hours:02}:{minutes:02}:{seconds:02}')