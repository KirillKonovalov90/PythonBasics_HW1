from math import sqrt
s = int(input('Сумма чисел равна: '))
p = int(input('Произведение чисел равно: '))

D = s*s - 4*p
if D > 0:
    x = int(s/2 - sqrt(D)/2)
    y = s - x
    print(f'первое число = {x}, второе = {y}')
elif D == 0:
    x = int(s / 2)
    print(f'первое число = второму и = {x}')
else:
    print('таких чисел не существует')