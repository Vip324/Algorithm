# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

import random

size_array = int(input(f'Введите длину массива : '))
# SIZE = 10
MIN_ITEM = 1
MAX_ITEM = 100
array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(size_array)]
array_2 = []

print()
print('Сгенерированный случайным образом Масив_1 : ')
print(array_1)

for i in range(size_array):
    if array_1[i] % 2 == 0:
        array_2.append(i)

print()
print('Масив_2 состоит из индексов четных элементов Массива_1 : ')
print(array_2)
