# Задача 1
# Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках практического задания первых трех уроков.
#

from random import randint
import timeit
import cProfile


def sort_to_bubble(m):
    mssv_l4 = [randint(-100, 100) for i in range(m)]

    n = len(mssv_l4)
    for i in range(n):

        for j in range(n - i - 1):
            a, b = mssv_l4[j], mssv_l4[j + 1]

            if a > b:
                mssv_l4[j], mssv_l4[j + 1] = b, a

    return mssv_l4


# m = int(input('Введите размерность массива '))
# sort_to_bubble(m)

print(timeit.timeit('sort_to_bubble(10)', number=100, globals=globals()))  # 0.005315481990692206
print(timeit.timeit('sort_to_bubble(100)', number=100, globals=globals()))  # 0.130509422000614
print(timeit.timeit('sort_to_bubble(1000)', number=100, globals=globals()))  # 11.673922312998911
print(timeit.timeit('sort_to_bubble(1000)', number=100, globals=globals()))  # 12.1929960760026

cProfile.run('sort_to_bubble(10)')
cProfile.run('sort_to_bubble(100)')
cProfile.run('sort_to_bubble(1000)')
cProfile.run('sort_to_bubble(10000)')