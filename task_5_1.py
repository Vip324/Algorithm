# Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за 4 квартал (т.е. 4 числа)
# для каждого предприятия. Программа должна определить
# среднюю прибыль (за год для всех предприятий) и отдельно
# вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.


from collections import namedtuple

num_fact = int(input('Какое количество предприятий вы хотите проанализировать : '))
Fact = namedtuple('Fact', 'name pr_1q pr_2q pr_3q pr_4q avr_pr')
real_fact = [Fact('', 0, 0, 0, 0, 0) for i in range(num_fact)]
looser_fact, best_fact = [], []
name = ''
pr_1q, pr_2q, pr_3q, pr_4q, avr_pr, avr_pr_all = 0, 0, 0, 0, 0, 0

for i in range(num_fact):
    name = input(f'Введите название предприятия номер {i + 1} : ')
    pr_1q = int(input('Введите прибыль первого квартала     : '))
    pr_2q = int(input('Введите прибыль второго квартала     : '))
    pr_3q = int(input('Введите прибыль третьего квартала    : '))
    pr_4q = int(input('Введите прибыль четвертого квартала  : '))
    avr_pr = (pr_4q + pr_3q + pr_2q + pr_1q) / 4
    avr_pr_all += avr_pr
    real_fact[i] = Fact(name, pr_1q, pr_2q, pr_3q, pr_4q, avr_pr)

avr_pr_all = avr_pr_all / num_fact
for i in range(num_fact):
    if real_fact[i].avr_pr <= avr_pr_all:
        looser_fact.append(real_fact[i])
    else:
        best_fact.append(real_fact[i])

print()
print('*' * 75)
print()
print(f'Средня прибыль по отрасли равнв  {avr_pr_all}')
print()
print('*' * 75)
print()
print('Предприятия с пибылью ниже или равной средней по отрасли : ')
print()
for i in range(len(looser_fact)):
    print(f'{looser_fact[i].name} со средней прибылью  {looser_fact[i].avr_pr}')
print()
print('*' * 75)
if len(best_fact) > 0:
    print()
    print('Предприятия с пибылью выше средней по отрасли : ')
    print()
    for i in range(len(best_fact)):
        print(f'Предприятие {best_fact[i].name} со средней прибылью  {best_fact[i].avr_pr}')
        print()
        print('*' * 75)
