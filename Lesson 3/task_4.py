# Задача 4
# Определить, какое число в массиве встречается чаще всего.
# Блок-схема - https://drive.google.com/file/d/1MrakisFgKl3rHGHVMkHnfA5Ny4s75HuW/view?usp=sharing


from random import randint

my_mssv = [randint(0, 9) for i in range(10)]
# my_mssv = [5, 1, 4, 4, 5, 5, 5, 4, 4, 1] # число 4 и 5 встречается по 4 раза
# my_mssv = [10, 1, 2, 3, 3, 3, 3, 3, 3, 5, 5, 5, 5, 5, 5, 4, 4, 4]
# my_mssv = [0, 1, 0, 0, 1, 1, 1, 1, 0, 0]  # число 0 встречается 5 раз
# my_mssv = [5, 1, 6, 7, 2, 0, 9, 4] # числа по 1 разу

num = my_mssv[0]
frequency_max = 0
print('Массив:', my_mssv)

n = len(my_mssv)

for i in range(n - 1):

    frequency = 1

    for j in range(i + 1, n):

        if my_mssv[i] == my_mssv[j]:
            frequency = frequency + 1

    if frequency > frequency_max:
        frequency_max = frequency


if frequency_max == 1:
    print('Все числа встречаются по', frequency_max, 'разу')
else:
    print('Число', my_mssv[i], 'встречается в массиве', frequency_max, 'раз')
