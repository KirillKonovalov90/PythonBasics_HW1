n = int(input('Введите желаемое число: '))
two = 2
answer = [1]

while two <= n:
    answer.append(two)
    two *= 2
    
print(answer)