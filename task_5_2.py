# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы
# которого — цифры числа. Например, пользователь ввёл A2 и C4F.
# Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque


# -------------------------------------------------------------------------
# Подготовка таблиц с данными
mat_sum = [['_' for _ in range(16)] for _ in range(16)]
# mat_mult = [['_' for _ in range(16)] for _ in range(16)]
num_hex = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
           'a', 'b', 'c', 'd', 'e', 'f']

for i in range(16):
    for j in range(16):
        mat_sum[i][j] = str(hex(i + j))[2:]
        # mat_mult[i][j] = str(hex(i * j))[2:]
# -------------------------------------------------------------------------

# -------------------------------------------------------------------------
# Функция сложение с переносом
def s_h_n(a, b, c):
    x = 0
    k = '0'
    x = mat_sum[num_hex.index(a)][num_hex.index(b)]
    x1, x2 = [], []
    if c == '0':
        if len(x) == 1:
            return x, k
        else:
            k = x[0]
            x = x[1]
            return x, k
    else:
        if len(x) == 1:
            x1 = s_h_n(x, c, '0')
            return x1[0], x1[1]
        else:
            x1 = s_h_n(x[1], c, '0')
            x2 = s_h_n(x[0], x1[1], '0')
            return x1[0], x2[0]
# -------------------------------------------------------------------------

print('Сложение шестнацитиричных чисел.')
print('*' * 32)
st_num_1 = input('Введите первое число : ')
st_num_2 = input('Введите второе число : ')

st_num_1 = deque(st_num_1)
st_num_2 = deque(st_num_2)

cont_up = '0'
spam_a = min(len(st_num_1), len(st_num_2))
spam_sum = ''
total_sum = deque()

for i in range(spam_a):
    q = []
    spam_sum = mat_sum[num_hex.index(st_num_1.pop())][num_hex.index(st_num_2.pop())]
    if len(spam_sum) == 1 and cont_up == '0':
        total_sum.appendleft(spam_sum)
    else:
        if cont_up == '0':
            cont_up = spam_sum[0]
            total_sum.appendleft(spam_sum[1])
        elif len(spam_sum) == 1 and cont_up != '0':
            q = s_h_n(cont_up, spam_sum, '0')
            cont_up = q[1]
            total_sum.appendleft(q[0])
        else:
            q = s_h_n(cont_up, spam_sum[1], '0')
            total_sum.appendleft(q[0])
            q = s_h_n(q[1], cont_up, '0')
            cont_up = q[0]

if len(st_num_1) == 0 and len(st_num_2) == 0:
    total_sum.appendleft(cont_up)

st_num_1 = max(st_num_1, st_num_2)

if cont_up == '0':
    total_sum.extendleft(st_num_1)
else:
    while cont_up != '0' and len(st_num_1) > 0:
        spam_sum = mat_sum[num_hex.index(st_num_1.pop())][num_hex.index(cont_up)]
        if len(spam_sum) == 1:
            total_sum.appendleft(spam_sum)
            if len(st_num_1) > 0:
                total_sum.extendleft(st_num_1)
            break
        else:
            total_sum.appendleft(spam_sum[1])
            cont_up = spam_sum[0]
        if len(st_num_1) < 1:
            total_sum.appendleft(cont_up)

print()
print(f'Результат сложения : {"".join(total_sum)}')
