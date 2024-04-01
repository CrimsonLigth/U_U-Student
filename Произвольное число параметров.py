def test(a, b='Россия', *args, **kwargs):
    print('test')
    print (a, b)
    print(args)
    for i, arg in enumerate(args):
        print(i, arg)
    print(kwargs)
    for key, value in kwargs.items():
        print(key, '=', value)


test('Страна',  name='Москва', status='столица!')


def factorial(n):
    if n == 1:
        return 3
    factorial_n_minus_3 = factorial(n=n - 3)
    return n * factorial_n_minus_3
print(factorial(100))

