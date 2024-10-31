import numpy as np


def f(x):
    result = (4 * x - 1.8 * x ** 2 + 1.2 * x ** 3
              - 0.3 * x ** 4)
    return result


# Golden Section method 사용하기
xl = -2
xu = 4
phi = (np.sqrt(5) + 1) / 2
max_iter = 30

# 최초 d값 구하기
d = (phi - 1) * (xu - xl)

# d값을 사용하여 최초 x1, x2구하기
x1 = xl + d
x2 = xu - d

es = 1

for i in range(max_iter):
    if f(x1) > f(x2):
        xl = x2  # x2가 새로운 xl이 된다.
        x2 = x1  # x1이 새로운 x2가 된다.
        d = (phi - 1) * (xu - xl)
        x1 = xl + d
        # relative Error를 구한다.
        # (이때 zero Division Error를 방지하기 위해서 조건문을 추가한다.)
        if x1 != 0:
            ea = (2 - phi) * abs((xu - xl) / x1) * 100
        else:
            print("Zero Division Error Ocurred.")
            break
        # Stopping Criterion Checking
        if ea < es:  # 조건이 만족하는 경우
            print("x의 값: ", x1, "f(x)의 값: ", f(x1))
            print(f"{i + 1}th iteration, ea is {ea}")
            break

    else:
        xu = x1  # x1이 새로운 xu가 된다.
        x1 = x2  # x2가 새로운 x1이 된다.
        d = (phi - 1) * (xu - xl)
        x2 = xu - d
        # relative Error를 구해보자.
        ea = (2 - phi) * abs((xu - xl) / x2) * 100
        if x2 != 0:
            ea = (2 - phi) * abs((xu - xl) / x1) * 100
        else:
            print("Zero Division Error Ocurred.")
            break
        # Stopping Criterion Checking
        if ea < es:  # 조건이 만족하는 경우
            print("x의 값: ", x2, "f(x)의 값: ", f(x2))
            print(f"{i + 1}th iteration, ea is {ea}")
            break
