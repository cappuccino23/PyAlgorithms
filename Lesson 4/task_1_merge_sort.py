# Задача 1
# Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках практического задания первых трех уроков.
# метод сортировки слияением

from random import randint
import timeit
import cProfile


def merge_sort(mssv_l4):
    if len(mssv_l4) > 1:

        mid = len(mssv_l4) // 2
        a = mssv_l4[:mid]  # левая сторона массива
        b = mssv_l4[mid:]  # правая сторона массива

        merge_sort(a)  # рекурсивно вызываем функцию merge_sort для каждого из массивов
        merge_sort(b)

        i = 0
        j = 0
        k = 0

        while i < len(a) and j < len(b):

            if a[i] < b[j]:
                mssv_l4[k] = a[i]
                i = i + 1
            else:
                mssv_l4[k] = b[j]
                j = j + 1

            k = k + 1

        while i < len(a):
            mssv_l4[k] = a[i]
            i = i + 1
            k = k + 1

        while j < len(b):
            mssv_l4[k] = b[j]
            j = j + 1
            k = k + 1

    return


def form_mass(m):
    mssv_l4 = [randint(-100, 100) for i in range(m)]
    merge_sort(mssv_l4)

# m = int(input('Введите номер простого числа: '))
# m = 20

#form_mass(m)

print(timeit.timeit('form_mass(10)', number=100, globals=globals()))  # 0.004359122001915239
print(timeit.timeit('form_mass(100)', number=100, globals=globals())) # 0.06010141401202418
print(timeit.timeit('form_mass(1000)', number=100, globals=globals())) # 0.7737665640015621
print(timeit.timeit('form_mass(10000)', number=100, globals=globals())) # 9.680613895994611

cProfile.run('form_mass(10)')
cProfile.run('form_mass(100)')
cProfile.run('form_mass(1000)')
cProfile.run('form_mass(10000)')