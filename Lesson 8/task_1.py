# Задача 1 Определить количество различных подстрок с использованием хеш-функции.
#
# Задача: на вход функции дана строка, требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.
import hashlib


def sub_str(mssv):
    bbb = []
    d = 0
    mdict = dict()
    hash_str = hashlib.sha1(mssv.encode('utf-8')).hexdigest()
    hash_space = hashlib.sha1(''.encode('utf-8')).hexdigest()

    for i in range(len(mssv)):
        bbb.append(hashlib.sha1(mssv[i].encode('utf-8')).hexdigest())
        for j in range(i, len(mssv)):
            s = (hashlib.sha1((mssv[i - 1:j + 1]).encode('utf-8')).hexdigest())
            if (s != hash_space) and (s != hash_str):
                bbb.append(hashlib.sha1(s.encode('utf-8')).hexdigest())


    for x in bbb:
        if x not in mdict:
            mdict[x] = 1
        else:
            mdict[x] = mdict[x] + 1

    for k, v in mdict.items():
        d = d + 1

    return print(f'Количество подстрок - {d-1}')


mssv = input('Введите строку: ')
# mssv = 'bosa'
print(f'Вывод строки: {mssv}')
sub_str(mssv)
