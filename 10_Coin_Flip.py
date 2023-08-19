n = int(input('Количество монет: '))
count_h = 0
count_t = 0
i = 1

# тут делаю через while чтобы защититься от неверных значений, вводимых пользователем
while i <= n:
    coin = int(input('Орёл 1, решка 0: '))
    if coin == 0:
        count_h += 1
        i += 1
    if coin == 1:
        count_t += 1
        i += 1
    elif coin != 1 and coin != 0: 
        print ('Ввведён неверный параметр,разрешены только 1 и 0')

print(count_h) if count_h < count_t else print(count_t)