# По введенному числу определяем букву алфавита

import sys

def show(obj):
    print(f'size = {sys.getsizeof(obj)}')
    if hasattr(obj, '__iter__'):
        if hasattr(obj, 'items'):
            for key, value in obj.items():
                show(key)
                show(value)
        elif not isinstance(obj, str):
            for item in obj:
                show(item)


def letter_v1(letter):
    if 1 <= letter <= 26:

        if letter == 1:
            print('Такому числу соотвествует буква алфавита - a')
        elif letter == 2:
            print('Такому числу соотвествует буква алфавита - b')
        elif letter == 3:
            print('Такому числу соотвествует буква алфавита - c')
        elif letter == 4:
            print('Такому числу соотвествует буква алфавита - d')
        elif letter == 5:
            print('Такому числу соотвествует буква алфавита - e')
        elif letter == 6:
            print('Такому числу соотвествует буква алфавита - f')
        elif letter == 7:
            print('Такому числу соотвествует буква алфавита - g')
        elif letter == 8:
            print('Такому числу соотвествует буква алфавита - h')
        elif letter == 9:
            print('Такому числу соотвествует буква алфавита - i')
        elif letter == 10:
            print('Такому числу соотвествует буква алфавита - j')
        elif letter == 11:
            print('Такому числу соотвествует буква алфавита - k')
        elif letter == 12:
            print('Такому числу соотвествует буква алфавита - l')
        elif letter == 13:
            print('Такому числу соотвествует буква алфавита - m')
        elif letter == 14:
            print('Такому числу соотвествует буква алфавита - n')
        elif letter == 15:
            print('Такому числу соотвествует буква алфавита - o')
        elif letter == 16:
            print('Такому числу соотвествует буква алфавита - p')
        elif letter == 17:
            print('Такому числу соотвествует буква алфавита - q')
        elif letter == 18:
            print('Такому числу соотвествует буква алфавита - r')
        elif letter == 19:
            print('Такому числу соотвествует буква алфавита - s')
        elif letter == 20:
            print('Такому числу соотвествует буква алфавита - t')
        elif letter == 21:
            print('Такому числу соотвествует буква алфавита - u')
        elif letter == 22:
            print('Такому числу соотвествует буква алфавита - v')
        elif letter == 23:
            print('Такому числу соотвествует буква алфавита - w')
        elif letter == 24:
            print('Такому числу соотвествует буква алфавита - x')
        elif letter == 25:
            print('Такому числу соотвествует буква алфавита - y')
        elif letter == 26:
            print('Такому числу соотвествует буква алфавита - z')

    else:
        print('Данному числу нельзя найти соответствие в английском алфавите')

    return


letter = int(input('Введите число от 1 до 26: '))
letter_v1(letter)

show(letter_v1)