# Задача 3
# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
# Блок-схема - https://drive.google.com/file/d/1EVjfVBiV0WAgJ0KhTbFDs31skxbVVBoe/view?usp=sharing

from random import randint

my_mssv = [randint(0, 100) for i in range(10)]
print('Исходный массив:', my_mssv)

mn = 0
mx = 0
max_el = my_mssv[0]
min_el = my_mssv[0]

for i in my_mssv:

    if i > max_el:
        max_el = i
        mx = my_mssv.index(i)

    elif i < min_el:
        min_el = i
        mn = my_mssv.index(i)

my_mssv[mx], my_mssv[mn] = my_mssv[mn], my_mssv[mx]

print('Максимальный элемент -', max_el, '\nМинимальный элемент -', min_el)
print('Массив с переставленными max и min элементами', my_mssv)



