# Найдите сумму цифр трехзначного числа.

# Пример:

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

print('Введите трехзначное число: ')
number = int(input())
sum = 0

while  number > 0:
    x = number % 10
    sum = sum + x 
    number = number // 10
    
print(sum)
