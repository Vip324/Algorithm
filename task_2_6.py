# В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться, больше или меньше
# введенное пользователем число, чем то, что загадано. Если
# за 10 попыток число не отгадано, вывести ответ.
import random

z = random.randint(0, 100)
i = 1
l = True

print('Угадайте число от 0 до 100. У Вас есть 10 попыток.')

while i <= 10 and l == True:
    n = int(input('Введите число : '))
    if n < z:
        print('Ваше число меньше. ')
        i += 1
    elif n > z:
        print('Ваше число больше. ')
        i += 1
    else:
        l = False
        print('Поздравляю! Вы его угадали. ')

if i == 11:
    print(f'Вам не удалось отгадать число! Это было - {z} .')
