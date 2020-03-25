import random
from random import randint


def quick_sort(mssv_l4):

    if len(mssv_l4) <= 1:
        return mssv_l4

    else:
        q = mssv_l4[0]

        s_mssv_l4 = []
        m_mssv_l4 = []
        e_mssv_l4 = []

        for n in mssv_l4:

            if n < q:
                s_mssv_l4.append(n)

            if n == q:
                m_mssv_l4.append(n)

            if n > q:
                e_mssv_l4.append(n)

    return quick_sort(s_mssv_l4) + m_mssv_l4 + quick_sort(s_mssv_l4)


mssv_l4 = [-31, 34, 36, -1, -50, -77, -87, 57, 46, -74]
mssv_l4 = [randint(-100, 100) for i in range(5)]
print(mssv_l4)

quick_sort(mssv_l4)
print(mssv_l4)
