# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

sum = 0
number = input('Введите число: ')
for i in number:
    if i.isdigit():
        sum += int(i)
print(sum)