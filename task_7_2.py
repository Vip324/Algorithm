# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

import random


# def shell_sort(array):
#     assert len(array) < 4000, "Массив слишком большой"
#
#     def new_increment(array):
#         inc = [1, 4, 10, 23, 57, 132, 301, 701, 1750]
#         while len(array) <= inc[-1]:
#             inc.pop()
#         while len(inc) > 0:
#             yield inc.pop()
#
#     for increment in new_increment(array):
#         for i in range(increment, len(array)):
#             for j in range(i, increment - 1, -increment):
#                 if array[j - increment] <= array[j]:
#                     break
#                 array[j], array[j - increment] = array[j - increment], array[j]


def merge(left, right):
    lst = []
    while left and right:
        if left[0] < right[0]:
            lst.append(left.pop(0))
        else:
            lst.append(right.pop(0))
    if left:
        lst.extend(left)
    if right:
        lst.extend(right)
    return lst


def mergesort(lst):
    assert len(lst) < 4000, "Массив слишком большой"
    if len(lst) >= 2:
        mid = int(len(lst) / 2)
        lst = merge(mergesort(lst[:mid]), mergesort(lst[mid:]))
    return lst


z = int(input('Введитеразмер масива для сортировки : '))
array_1 = [random.random() * 50 for i in range(z)]
print(array_1)
mergesort(array_1)
print(mergesort(array_1))
