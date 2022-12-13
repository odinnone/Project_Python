# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

numbers = []
n = int(input('Введите число: '))
for i in range(2, n, 1):
    count = 0
    for j in range(1, i, 1):
        if i % j == 0:
            count += 1
    if count == 1 and n % i == 0:
        numbers.append(i)
print(numbers)