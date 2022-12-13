# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint
numbers = []
f =[]
n = int(input('Введите кол-во элементов: '))
for i in range(n):
    numbers.append(randint (0,10))
    f.append(0)
print(numbers)
p = []
for i in range(0, n, 1):
    count = 0
    for j in range(i+1, n, 1):
        if numbers[i] == numbers[j]:
            count += 1
            f[j] = -1
    if count == 0 and f[i] != -1:
        p.append(numbers[i])
print(p)