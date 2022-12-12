# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.

from random import randint
numbers = []
n = int(input('Введите кол-во элементов: '))
for i in range(n):
    numbers.append(randint (-n,n))
print(numbers)
x = int(input('Позиция первого элемента: '))
y = int(input('Позиция второго элемента: '))
for i in range(len(numbers)):
    p = numbers[x -1]*numbers[y - 1]
print(p)