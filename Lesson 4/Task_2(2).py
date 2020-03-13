# Задача 2_2
# Написать два алгоритма нахождения i-го по счёту простого числа.
# Использовать алгоритм решето Эратосфена
# Проанализировать скорость и сложность алгоритмов. Результаты анализа сохранить в виде комментариев в файле с кодом.
# Блок-схема -

import timeit


def resheto_eratosfena(m):
    c = 0  # количество делителей

    for i in range(2, m * m):

        for j in range(2, i):

            if i % j == 0:
                c = c + 1

        if c == 0:
            a.append(i)
        else:
            c = 0

    for i in range(0, len(a) + 1):

        if i == m:
            id = a[i - 1]

    return id


# m = int(input('Введите номер простого числа: '))
a = []

# resheto_eratosfena(m)

print(timeit.timeit('resheto_eratosfena(10)', number=100, globals=globals()))  # 0.06177425300120376
print(timeit.timeit('resheto_eratosfena(100)', number=100, globals=globals()))  #
print(timeit.timeit('resheto_eratosfena(1000)', number=100, globals=globals()))  #
print(timeit.timeit('resheto_eratosfena(10000)', number=100, globals=globals()))  #
