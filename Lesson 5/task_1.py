# Задача 1
# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import deque

a = int(input('Введите количество предприятий '))
i = 1
profit = 0
company = {}
avg_1

for i in range(1, a+1):

    c = input(f'Введите название {i} предприятия: ')

    for j in range(1, 5):
        b = int(input(f'Введите прибыль за {j} квартал: '))
        profit = (profit + b)

    company[c] = profit

for v in company:

    avg_1 = company.values() + avg_1

avrg_year = avg_1 / 4

print(company)
