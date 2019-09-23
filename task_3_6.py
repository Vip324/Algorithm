# В одномерном массиве найти сумму элементов, находящихся между
# минимальным и максимальным элементами. Сами минимальный
# и максимальный элементы в сумму не включать.

import random

SIZE = 10
MIN_ITEM = 1
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print('Сгенерирован масив случайных чисел : ')
print(array)

val_min = [0, array[0]]
val_max = [0, array[0]]
sum_ = 0

for i in range(1, SIZE):
    if array[i] > val_max[1]:
        val_max[1] = array[i]
        val_max[0] = i
    elif array[i] < val_min[1]:
        val_min[1] = array[i]
        val_min[0] = i

if val_max[0] > val_min[0]:
    for j in range(val_min[0] + 1, val_max[0]):
        sum_ += array[j]
elif val_max[0] < val_min[0]:
    for j in range(val_max[0] + 1, val_min[0]):
        sum_ += array[j]

if sum_ != 0:
    print(f'Сумма чисел в масиве между мин.({val_min[1]}) и мак.({val_max[1]}) занчением равна {sum_}.')
else:
    print(f'Мак. и мин. значения в масиве находятся рядом на {val_max[0] + 1} и {val_min[0] + 1} местах.')
