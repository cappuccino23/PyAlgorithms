#Задача 1
# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
# Блок-схема - https://drive.google.com/open?id=1YlfSxx4N27j73qq5emXOdcwZQW38Mwqe

number = list(input('Введите трехзначное число: '))

a = int(number[0])
b = int(number[1])
c = int(number[2])

sum = a + b + c
multiplication = a * b * c


print('Число:', sum)
print('Число:', multiplication)
