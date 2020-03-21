# По введенному числу определяем букву алфавита

import sys


def letter_v2(lttr):
    for key in letter:
        if lttr == key:
            print(f'Такому числу соотвествует буква алфавита - {letter.get(key)}')


d = 0
letter = {1: 'a',
          2: 'b',
          3: 'c',
          4: 'd',
          5: 'e',
          6: 'f',
          7: 'g',
          8: 'h',
          9: 'i',
          10: 'j',
          11: 'k',
          12: 'l',
          13: 'm',
          14: 'n',
          15: 'o',
          16: 'p',
          17: 'q',
          18: 'r',
          19: 's',
          20: 't',
          21: 'u',
          22: 'v',
          23: 'w',
          24: 'x',
          25: 'y',
          26: 'z'
          }

lttr = int(input('Введите число от 1 до 26: '))

letter_v2(lttr)

for s in [letter, lttr, d]:
    d = sys.getsizeof(s) + d

print(f'\nВыделено примерно {d} байт памяти под переменные')
