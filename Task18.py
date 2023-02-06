# Задача 18
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

# Пример:

# 5
# 1 2 3 4 5
# 6
# -> 5

random_list=[]
n = int(input('Введите количество элементов массива: '))
number = int(input('Введите число для поиска близкого по велечине элемента в списке: '))
from random import randint
for i in range(n):
    random_list.append(randint(1,9))
print(random_list)

chmass = [i for i in random_list if i != number]
print(chmass)

res = 0
for i in range(len(chmass)):
    if abs(chmass[i] - number) < abs(res - number):
        res = chmass[i]
        
print(res)