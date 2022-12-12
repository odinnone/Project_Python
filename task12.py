# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import randint
numbers = []
n = int(input('Введите кол-во элементов: '))
for i in range(n):
    numbers.append(randint (1,10))
print(numbers)
p = []
if n % 2 == 0: m = n // 2
else: m = n // 2 + 1
for i in range(0, m, 1):
    a = numbers[i] * numbers[n-i-1]
    p.append(a)
print(p)