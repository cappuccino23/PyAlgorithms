# По введенному числу определяем букву алфавита

import sys
d = 0
letter = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

lttr = int(input('Введите число от 1 до 27: '))

for i in range(0, len(letter)):
    if lttr == i:
        print(f'Такому числу соотвествует буква алфавита - {letter[i-1]}')


for s in [letter, lttr, d]:
    d = sys.getsizeof(s) + d

print(d)
