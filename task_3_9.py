# Найти максимальный элемент среди минимальных
# элементов столбцов матрицы.

import random

SIZE = 10
MIN_ITEM = 1
MAX_ITEM = 100
array = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)] for _ in range(SIZE)]

val_min_max = 0

print(f'Сгенерированная матрица : ')
print()
for j in range(SIZE):
    print(*array[j], sep='\t')
    val_min = array[0][j]
    for i in range(SIZE):
        if array[i][j] < val_min:
            val_min = array[i][j]
    if val_min > val_min_max or val_min_max == 0:
        val_min_max = val_min

print()
print(f'Мак. значение из мин. элементов столбцов матрицы равно {val_min_max}.')