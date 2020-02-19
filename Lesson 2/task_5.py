# Задача 5

# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

# блок-схема - https://drive.google.com/file/d/1jlGwJhgdmOs9Jr9DRatZQIxulClJAX6u/view?usp=sharing

print('Для завершения ввода введите 0')
number = int(input('Введите число: '))

sum_numb = 0 #сумма цифр числа
max_sum_numb = 0 #максимальная сумма цифр числа

while number != 0:

    max_n = number #фиксируем число, которому соответствует сумма его цифр
    sum = 0

    while number > 0:

        sum = sum + (number % 10)
        number = number // 10 #уменьшаем number через остаток от деления

    if sum > sum_numb:

        sum_numb = sum
        max_sum_numb = max_n

    number = int(input('Введите число: '))

print('Число', max_sum_numb, 'имеет максимальную сумму цифр:', sum_numb)
