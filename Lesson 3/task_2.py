# Задача 2
# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5,
# (индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.
# Блок-схема - https://drive.google.com/file/d/1QYBPAOgWooxXLu_-IhTI9qV1bElCwiFo/view?usp=sharing

from random import randint

# my_mssv = [randint(0, 100) for i in range(10)]
# my_mssv = [8, 3, 15, 6, 4, 2] - [0, 3, 4, 5]

my_mssv = [22, 87, 46, 23, 34, 81, 31, 22, 24, 21]

n = 0
mssv_2 = []

print('Массив:', my_mssv)

m = len(my_mssv)

for i in range(m):

    if my_mssv[i] % 2 == 0:
        mssv_2.append(i)

print("Индексы четных элементов первого массива:", mssv_2)
