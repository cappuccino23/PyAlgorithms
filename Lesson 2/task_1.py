#Задача 1

# Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна
# завершаться, а должна запрашивать новые данные для вычислений. Завершение программы должно
# выполняться при вводе символа '0' в качестве знака операции. Если пользователь вводит неверный
# знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и снова запрашивать
# знак операции. Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.

# Блок-схема - https://drive.google.com/open?id=1YlfSxx4N27j73qq5emXOdcwZQW38Mwqe

number = list(input('Введите трехзначное число: '))

n = int(number[0])
m = int(number[1])
d = int(number[2])

sum = n + m + d
multiplication = n * m * d


print('Число:', sum)
print('Число:', multiplication)