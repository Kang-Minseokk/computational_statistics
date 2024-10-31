import numpy as np


def func1(x):
    result = -12 - 21 * x + 18 * x ** 2 - 2.75 * x ** 3
    return result


def Kang4375(func, xl, xu, Ead=1e-7):
    # 구간 내에 근이 없는 경우 종료하기
    if func(xl) * func(xu) > 0:
        return 'Initial estimates do not bracket solution.'

    # 반복해야 하는 수 정하기
    n = int(np.ceil(np.log2((xu - xl) / Ead)))
    xm = (xu + xl) / 2

    for i in range(n):
        if func(xl) * func(xm) < 0:
            xu = xm
        else:
            xl = xm
        old_xm = xm
        xm = (xu + xl) / 2

    root = xm
    # ea 구하기
    ea = abs((xm - old_xm) / xm)
    # Ea 구하기
    Ea = (xu - xl) / 2 ** (i + 1)

    return root, Ea, ea, n


print(Kang4375(func1, -3, 10))