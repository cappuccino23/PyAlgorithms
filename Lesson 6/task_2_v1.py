# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import sys
from random import randint

my_mssv = [randint(-100, 100) for i in range(1000)]

d = 0
sum_el = 0
mssv = []
mx = 0
mn = 0
max_el = my_mssv[0]
min_el = my_mssv[0]

for i in my_mssv:
    if i > max_el:
        max_el = i
        mx = my_mssv.index(i)

    if i < min_el:
        min_el = i
        mn = my_mssv.index(i)

print('max -', max_el, '\nmin -', min_el)

if mx > mn:

    for i in my_mssv[mn + 1:mx]:
        mssv.append(i)

else:
    for i in my_mssv[mx + 1:mn]:
        mssv.append(i)

for i in mssv:
    sum_el = sum_el + i

print('Сумма элементов между min и max, не включающая их =', sum_el)

# считаем примерное выделение памяти под переменные

for s in [my_mssv, mssv, sum_el, mx, mn, max_el, min_el, d]:
    d = sys.getsizeof(s) + d

print(f'\nВыделено {d} байт памяти под переменные')
