# Задача 1

import sys

# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
# ● выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
# ● написать 3 варианта кода (один у вас уже есть);
# ● проанализировать 3 варианта и выбрать оптимальный;
# ● результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл с кодом. Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
# ● написать общий вывод: какой из трёх вариантов лучше и почему.
# Надеемся, что вы не испортили программы, добавив в них множество sys.getsizeof после каждой переменной, а проявили творчество, фантазию и создали универсальный код для замера памяти.

# пояснения по дз
# версия Python
# Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
print(f'Версия Python {sys.implementation}')

# версия OS
# Microsoft Windows [Version 10.0.18363.720]
print(f'Версия OS {sys.platform}, {sys.getwindowsversion()}')

# Выводы:
# размер выделяемой памяти довольно сильно зависит от типа выбранных данных.
# Т.е. для задачи task_1 наиболее оптимальным будет вариант 1, но там достаточно много повторяющегося кода,
# поэтому в данном случае целесообразнее выбрать третий вариант.
#
# task_1_v1 size = 72 байт
# task_1_v2 size = 662 байт
# task_1_v2 size = 158 байт
#
# Задача task_2_v1 ля визуализации того как могут переменные менять конечный размер занимаемой памяти
# т.е в зависимости от размере входного массива были проанализированы массивы на 50, 100, 1000.
# Изменение зависит от формируемого массива (он будет иметь разный размер, так как в каждом случае мы генерируем
# разный массив) при условиях в выбранной задаче
# при n = 50 размер занимаемой памяти -  418, 526, 402, 570, 450 байт в каждом из 5 случаев,
# при n = 100 размер занимаемой памяти -  762, 594, 810, 718, 610 байт в каждом из 5 случаев,
# при n = 1000 размер занимаемой памяти -  6254, 4698, 4922, 6050, 7350 байт в каждом из 5 случаев,
#

