# Поиск наибольшей общей подпоследовательности


import cProfile
import random
import string


def las1(st1, st2):  # O(n*m + z^2) - итого
    result = ''
    i = 0
    while i < len(st1):  # O(n*m) - один проход по матрице
        j = 0
        while j < len(st2):
            if st1[i] == st2[j]:
                result = result + st1[i]
            j += 1
        i += 1

    result = ''.join(sorted(set(result), key=result.index))  # O(z^2) - ??? сортировка и проход по списку совпадений
    return result


def main(n):
    N = n
    a = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N * 5))
    b = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))

    las1(a, b)


cProfile.run('main(2000)')

# 1    0.003    0.003    0.004    0.004 task_4_1_2.py:9(las1) n=50
# 1    0.013    0.013    0.016    0.016 task_4_1_2.py:9(las1) n=100
# 1    0.030    0.030    0.038    0.038 task_4_1_2.py:9(las1) n=150
# 1    0.053    0.053    0.067    0.067 task_4_1_2.py:9(las1) n=200
# 1    0.081    0.081    0.103    0.103 task_4_1_2.py:9(las1) n=250

# 1    1.380    1.380    1.774    1.774 task_4_1_2.py:9(las1) n=1000
# 1    5.634    5.634    7.224    7.224 task_4_1_2.py:9(las1) n=2000
