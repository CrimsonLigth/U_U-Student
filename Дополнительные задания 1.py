years = int(input('Введите год'))
if years % 4 == 0 and years % 100 != 0 or years % 400 == 0:
    print ('Високосный год')
else:
    print ('Не високосный год')





