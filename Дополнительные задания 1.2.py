weight = int(input('Введите вес посылки в кг '))
coast = 20
if weight < 2:
    print('Стоимость доставки', coast, 'рублей')
if weight == 2:
    coast += 20
    print('Стоимость доставки', coast, 'рублей')
if weight == 3:
    coast += 40
    print('Стоимость доставки', coast, 'рублей')
if weight == 4:
    coast += 60
    print('Стоимость доставки', coast, 'рублей')
if weight == 5:
    coast += 80
    print('Стоимость доставки', coast, 'рублей')
if weight == 6:
    coast += 100
    print('Стоимость доставки', coast, 'рублей')
if weight == 7:
    coast += 120
    print('Стоимость доставки', coast, 'рублей')
if weight == 8:
    coast += 140
    print('Стоимость доставки', coast, 'рублей')
if weight == 9:
    coast += 160
    print('Стоимость доставки', coast, 'рублей')
if weight == 10:
    coast += 180
    print('Стоимость доставки', coast, 'рублей')
if weight > 10:
    coast = 200
    print('Стоимость доставки', coast, 'рублей')