# Задача 10
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, 
# которые нужно перевернуть.

# Пример:

# 5 -> 1 0 1 1 0
# 2

from random import randint
numcoin = int(input('Введите количество монеток: '))
num0 = 0
num1 = 0
for _ in range(numcoin):
    coin = randint(0, 1)
    print(coin, end = ' ')
    if coin > 0:
        num1 += 1
    else: num0 +=1
print()
if num1 > num0:
    print(f'необходимо перевернуть {num0}')
else: print(f'необходимо перевернуть {num1}')
