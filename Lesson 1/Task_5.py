# Задача 5
# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
# Блок-схема - https://drive.google.com/file/d/1EXhyCoRhRyUfAk3vP615F2EMn_I-eOry/view?usp=sharing

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

if b < a < c or c < a < b:
    print('Среднее:', a)
elif a < b < c or c < b < a:
    print('Среднее:', b)
else:
    print('Среднее:', c)