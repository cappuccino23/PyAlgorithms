# Задача 6

# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

# блок-схема - https://drive.google.com/file/d/1G5CjRwyDUADsUcRmI3bdLPxXmuSmRKk-/view?usp=sharing


a = (input('Введите число: '))
b = (input('Введите цифру, которую хотите посчитать: '))
c = 0


for i in a:

    if int(i) == int(b):
        c = c + 1

print('Количество цифр:', c)