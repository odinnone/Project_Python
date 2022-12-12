# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

from random import uniform
numbers = []
n = int(input('Введите кол-во элементов: '))
for i in range(n):
    m = uniform(0, 10)
    numbers.append(round(m, 2))
print(numbers)
print(round(max(numbers) - min(numbers), 2))