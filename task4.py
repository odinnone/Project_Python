# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

import math
print('Введите координаты точки A(x1, y1)')
x1 = int(input())
y1 = int(input())
print('Введите координаты точки B(x2, y2)')
x2 = int(input())
y2 = int(input())
d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print('Расстояние между точками A и B -', d)