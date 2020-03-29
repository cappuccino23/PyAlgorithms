mssv = input('Введите строку: ')
# mssv = 'bosa'
print(f'Вывод строки: {mssv}')
d = 0
bbb = []

for i in range(len(mssv)):
    bbb.append(mssv[i])
    for j in range(i, len(mssv)):
        s = mssv[i - 1:j + 1]
        if (s != '') and (s != mssv):
            bbb.append(s)

print(bbb)

mdict = dict()

for x in bbb:
    if x not in mdict:
        mdict[x] = 1
    else:
        mdict[x] = mdict[x] + 1

print(mdict)

for k, v in mdict.items():
    d = d + 1
print(d)
