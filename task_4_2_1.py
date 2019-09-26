# Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход
# натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.

import cProfile


# Вариант 1
# _______________________________________________________________________

def fun_1(n):  # O(6*n^2)
    m_easy_num = [i for i in range(2, n * 11)]  # O(11*n) - формирование масива достаточного для поиска n<10 000

    # m_easy_num = []
    # for i in range(2, n * 11):
    #     m_easy_num.append(i)

    find_easy_num_1 = 0
    num_for = 0
    i = 0
    logic_val = True

    while logic_val:  # O(11*n/2 * n)=O(11/2*n^2) - n раз проход по остатку масива от n-го числа

        if m_easy_num[i] != 0 and i != len(m_easy_num):
            for j in range(i + 1, len(m_easy_num)):
                if m_easy_num[j] % m_easy_num[i] == 0:
                    m_easy_num[j] = 0
            num_for += 1

        i += 1

        if i == len(m_easy_num) or num_for == n:
            find_easy_num_1 = m_easy_num[i - 1]
            logic_val = False

    return find_easy_num_1


def main(q):
    n1 = q
    fun_1(n1)


cProfile.run('main(2000)')

# 1    0.003    0.003    0.003    0.003 task_4_2_1.py:12(fun_1) q=50
# 1    0.016    0.016    0.016    0.016 task_4_2_1.py:12(fun_1) q-100
# 1    0.027    0.027    0.027    0.027 task_4_2_1.py:12(fun_1) q=150
# 1    0.056    0.056    0.056    0.056 task_4_2_1.py:12(fun_1) q=200
# 1    0.077    0.077    0.078    0.078 task_4_2_1.py:12(fun_1) q=250

# 1    1.046    1.046    1.048    1.048 task_4_2_1.py:12(fun_1) q=1000
# 1    3.953    3.953    3.956    3.956 task_4_2_1.py:12(fun_1) q=2000
