# Задача 4

# В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться больше или меньше
# введенное пользователем число, чем то, что загадано.
# Если за 10 попыток число не отгадано, то вывести загаданное число.

# блок-схема - https://drive.google.com/file/d/1lR0WlLB6C3yPDoC4c8KzO_NAw8XXxEyA/view?usp=sharing

import random

random_number = random.randint(0, 100)


for i in range(10):

    number = int(input('Введите число: '))

    if random_number == number:
        print('Вы угадали! Число = ', random_number)
    else:
        if random_number > number:
            print('Число больше загаданного')
        else:
            print('Число меньше загаданного')

print('Как жаль, вы не угадали! Число было', random_number)

