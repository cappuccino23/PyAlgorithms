#Задача 1
# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
# Блок-схема - https://drive.google.com/open?id=1YlfSxx4N27j73qq5emXOdcwZQW38Mwqe

number = list(input('Введите трехзначное число: '))

n = int(number[0])
m = int(number[1])
d = int(number[2])

sum = n + m + d
multiplication = n * m * d


print('Число:', sum)
print('Число:', multiplication)