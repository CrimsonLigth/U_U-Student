weight = int(input('Введите вес посылки в кг '))
coast = 50
if weight < 2:
    print('Стоимость доставки', coast, 'рублей')
if weight > 2 and weight <= 10:
    print('Стоимость доставки', coast + (weight - 2) * 20, 'рублей')
else:
    print('Стоимость доставки', 200, 'рублей')
