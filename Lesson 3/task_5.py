# Задача 5
# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
# Блок-схема - https://drive.google.com/file/d/1BENNIygfWRsItgXe7baFrWQXqRV-tQIA/view?usp=sharing

from random import randint

#my_mssv = [39, -32, -16, 30, -85, 83, 83, -44, 39]
my_mssv = [randint(-100, 100) for i in range(10)]
print('Исходный массив:', my_mssv)

position = -1
min_el = 0

for i in my_mssv:

    if i < 0 and position == -1:
        min_el = i
        position = my_mssv.index(i)

    elif min_el < i < 0:
        min_el = i
        position = my_mssv.index(i)

print('Позиция максимального отрицательного элемента - ', position + 1)
print('Максимальный отрицательный элемент - ', min_el)
