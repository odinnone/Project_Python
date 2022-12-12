# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

from random import randint
numbers = []
n = int(input('Введите кол-во элементов: '))
for i in range(n):
    numbers.append(randint (0,10))
print(numbers)
s = 0
for i in range(1, len(numbers), 2):
    s = s + numbers[i]
print(s)