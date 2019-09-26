# Поиск наибольшей общей подпоследовательности

import cProfile
import random
import string


def las(st1, st2):  # O(2n*m + n+m) - итого
    m = [[0] * (len(st1) + 1) for _ in range(len(st2) + 1)]  # O(n*m) - обход матрицы

    for i, item1 in enumerate(st2, start=1):  # O(n*m) - обход матрицы
        for j, item2 in enumerate(st1, start=1):
            if item1 == item2:
                m[i][j] = m[i - 1][j - 1] + 1
            else:
                m[i][j] = max(m[i - 1][j], m[i][j - 1])

    result = []
    i, j = len(st2), len(st1)

    while i > 0 and j > 0 and m[i][j] != 0:  # O(n+m) - обход результата
        if m[i][j] == m[i][j - 1] and m[i][j] > m[i - 1][j - 1] and m[i][j] > m[i - 1][j]:
            j -= 1
        elif m[i][j] == m[i - 1][j] and m[i][j] > m[i - 1][j - 1] and m[i][j] > m[i][j - 1]:
            i -= 1
        elif m[i][j] > m[i - 1][j - 1] and m[i][j] > m[i - 1][j] and m[i][j] > m[i][j - 1]:
            result.append(st2[i - 1])
            i, j = i - 1, j - 1
        else:
            i, j = i - 1, j - 1

    result.reverse()
    result = ''.join(result)
    return result


def main(n):
    N = n
    a = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N * 5))
    b = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))

    las(a, b)


cProfile.run('main(2000)')

# 1    0.005    0.005    0.008    0.008 task_4_1_1.py:8(las)   n=50
# 1    0.020    0.020    0.031    0.031 task_4_1_1.py:8(las)   n=100
# 1    0.044    0.044    0.067    0.067 task_4_1_1.py:8(las)   n=150
# 1    0.075    0.075    0.115    0.115 task_4_1_1.py:8(las)   n=200
# 1    0.119    0.119    0.183    0.183 task_4_1_1.py:8(las)   n=250

# 1    1.968    1.968    2.975    2.975 task_4_1_1.py:8(las)   n=1000
# 1    8.050    8.050   12.135   12.135 task_4_1_1.py:8(las)   n=2000
