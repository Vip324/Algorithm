# Среди натуральных чисел, которые были введены,
# найти наибольшее по сумме цифр. Вывести
# на экран это число и сумму его цифр.

st_max = ''
s_max = 0
l = True

while l:
    st_test = input()
    s_test = 0
    if int(st_test) != 0:
        for i in st_test:
            s_test = s_test + int(i)
        if s_test > s_max:
            s_max = s_test
            st_max = st_test
    else:
        l = False

print(f'Наибольшая сумма цифр у числа {st_max} равна {s_max}.')