# Задача 4
# Определить, какое число в массиве встречается чаще всего.
# Блок-схема -


from random import randint

my_mssv = [randint(0, 9) for i in range(10)]
#my_mssv = [5, 1, 4, 4, 7, 2, 8, 4, 4, 1] # число 4 встречается 4 раза
#my_mssv = [0, 1, 0, 0, 1, 1, 1, 1, 0, 0] # число 0 встречается 3 раза

num = my_mssv[0]
frequency_m = 0
print('Массив:', my_mssv)

n = len(my_mssv)

for i in range(n):

    frequency = 1

    for j in range(n - i):

        if my_mssv[i] == my_mssv[j]:
            frequency = frequency + 1

    if frequency > frequency_m:
        frequency_m = frequency


num = my_mssv[i]

print('число - ', num, 'встречается в массиве -', frequency_m, 'раз')





