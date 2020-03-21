# Задача 2
# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными
# числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random


def merge_sort(mssv):
    if len(mssv) > 1:

        mid = len(mssv) // 2
        a = mssv[:mid]  # левая сторона массива
        b = mssv[mid:]  # правая сторона массива

        merge_sort(a)  # рекурсивно вызываем функцию merge_sort для каждого из массивов
        merge_sort(b)

        i = 0
        j = 0
        k = 0

        while i < len(a) and j < len(b):

            if a[i] < b[j]:
                mssv[k] = a[i]
                i = i + 1
            else:
                mssv[k] = b[j]
                j = j + 1

            k = k + 1

        # склеиваем массивы
        while i < len(a):
            mssv[k] = a[i]
            i = i + 1
            k = k + 1

        while j < len(b):
            mssv[k] = b[j]
            j = j + 1
            k = k + 1

    return


def prnt_mssv(mssv):
    for i in mssv:
        print('%.3f' % i, end=' ')


# m = int(input('Введите размерность массива: '))
mssv = [random.uniform(0, 50) for i in range(10)]

print('Исходный массив: ')
prnt_mssv(mssv)

merge_sort(mssv)

print(f'\n\nОтсортированный массив: ')
prnt_mssv(mssv)
