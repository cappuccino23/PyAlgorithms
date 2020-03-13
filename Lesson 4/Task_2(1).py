# Задача 2_2
# Написать два алгоритма нахождения i-го по счёту простого числа.
# - Без использования Решета Эратосфена;
#  Проанализировать скорость и сложность алгоритмов. Результаты анализа сохранить в виде комментариев в файле с кодом.

import timeit
import cProfile


def proverka(n): # проверяем простоту числа
    a = 2

    while n % a != 0:
        a = a + 1

    return a == n


def mas_prost(m, n): # заполняем массив простыми числами

    while len(b) <= m:

        if proverka(n) == True:
            b.append(n)

        n = n + 1

    return b


# m = int(input('введите число '))
b = []
n = 2
c = 0

#print(timeit.timeit('mas_prost(10,n)', number=100, globals=globals()))  # 9.328100713901222e-05
#print(timeit.timeit('mas_prost(100,n)', number=100, globals=globals()))  # 0.003845740997348912
#print(timeit.timeit('mas_prost(1000,n)', number=100, globals=globals()))  # 0.4364124559942866
#print(timeit.timeit('mas_prost(10000,n)', number=100, globals=globals()))  # 56.662043204007205

cProfile.run('mas_prost(10,n)')
cProfile.run('mas_prost(100,n)')
cProfile.run('mas_prost(1000,n)')
cProfile.run('mas_prost(10000,n)')