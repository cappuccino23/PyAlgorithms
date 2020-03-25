# Задача 2_2
# Написать два алгоритма нахождения i-го по счёту простого числа.
# Использовать алгоритм решето Эратосфена
# Проанализировать скорость и сложность алгоритмов. Результаты анализа сохранить в виде комментариев в файле с кодом.
# Блок-схема -

import timeit
import cProfile


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

#print(timeit.timeit('resheto_eratosfena(10)', number=100, globals=globals()))  # 0.060025059996405616
#print(timeit.timeit('resheto_eratosfena(50)', number=100, globals=globals()))  # 33.03356583999994
#print(timeit.timeit('resheto_eratosfena(100)', number=100, globals=globals()))  # 592.7037572080008
#print(timeit.timeit('resheto_eratosfena(150)', number=100, globals=globals()))  #


cProfile.run('resheto_eratosfena(10)')
cProfile.run('resheto_eratosfena(50)')
cProfile.run('resheto_eratosfena(100)')
