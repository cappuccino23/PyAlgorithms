# Задача 3
# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
# которые не меньше медианы, в другой — не больше медианы.
#
# Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
# используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).

from random import randint, random, choice


def sort_to_bubble(mssv):
    n = len(mssv)
    for i in range(n):

        for j in range(n - i - 1):
            a, b = mssv[j], mssv[j + 1]

            if a > b:
                mssv[j], mssv[j + 1] = b, a

    return


# mssv = [95, 13, 76, 92, 73]
# [4, 13, 30, 44, 64, 73, 76, 77, 92, 95, 100]  медиана - 73

m = int(input('Введите число: '))
mssv = [randint(1, 100) for i in range(2 * m + 1)]
print(mssv)

a = 0
b = 0

# Нужно сравнить элементы относительно выбранной медианы в цикле.
lenght_mssv = len(mssv)

for i in range(lenght_mssv):

    median = choice(mssv)

    for j in range(i + 1, lenght_mssv):

        if median >= mssv[j]:
            a = a + 1

        if median < mssv[j]:
            b = b + 1

    if a == b:
        median = mssv[i]
        print('медиана - ', median)
    else:
        a = 0
        b = 0


# часть СТРОГО для проверки и сравнения результатов
sort_to_bubble(mssv)
print('После сортировки: медиана - ', mssv[len(mssv) // 2])
