# В массиве случайных целых чисел поменять местами
# минимальный и максимальный элементы.

import random

SIZE = 10
MIN_ITEM = 1
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print('Сгенерирован масив случайных чисел : ')
print(array)

val_min = [0, array[0]]
val_max = [0, array[0]]

for i in range(1, SIZE):
    if array[i] > val_max[1]:
        val_max[1] = array[i]
        val_max[0] = i
    elif array[i] < val_min[1]:
        val_min[1] = array[i]
        val_min[0] = i

array[val_max[0]] = val_min[1]
array[val_min[0]] = val_max[1]

print()
print(f'Минимальный элемент {val_min[1]} находится на {val_min[0] + 1} месте')
print(f'Максимальный элемент {val_max[1]} находится на {val_max[0] + 1} месте')
print()
print('Максимальный и минимальный элементы поменяны местами : ')
print(array)
