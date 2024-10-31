import math
# (a) 그래프를 그려서 확인하기

import numpy as np
import matplotlib.pyplot as plt

# x 값의 범위 설정
x = np.linspace(-2, 5, 400)

# 주어진 함수: 7 * sin(x) * e ** (-x) - 1
y = 7 * np.sin(x) * np.exp(-x) - 1

# 그래프 그리기
plt.plot(x, y, label='7 * sin(x) * e^(-x) - 1')

# 그래프 꾸미기
plt.title("Graph of 7 * sin(x) * e^(-x) - 1")
plt.xlabel("x")
plt.ylabel("y")
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(True)
plt.legend()

# 그래프 출력
plt.show()


# (b) Wegstein Method 사용하기
def g(x):
    result = 7 * np.sin(x) * math.e ** (-x) - 1 + x
    return result


x0 = 0.1
x1 = 0.2
for i in range(4):
    x_next = (x1 * g(x0) - x0 * g(x1)) / (x1 - x0 -
                                          g(x1) + g(x0))
    print(f"{i + 1}th Iteration")
    print("X i-1 = ", x0)
    print("X i = ", x1)
    print("X i+1 = ", x_next, "\n")

    x0 = x1
    x1 = x_next

# (c) Newton - Raphson Method Using
def f(x) :
    result = 7 * np.sin(x) * math.e ** (-x) - 1
    return result

def grad_f(x) :
    result = (7 * np.cos(x) * math.e ** (-x) - 7 *
              np.sin(x) * math.e ** (-x))
    return result

x_previous = 0.3
for i in range(4) :
    x_next = x_previous - f(x_previous) / grad_f(x_previous)
    print(f"{i+1}th Iteration")
    print("x_next: ", x_next, "\n")
    x_previous = x_next

# (d) Modified Secant Method Using
x_previous = 0.3
delta_value = 0.001

for i in range(4) :
    x_next = (x_previous - (delta_value * f(x_previous)) /
              (f(x_previous + delta_value) - f(x_previous)))
    print(f"{i+1}th Iteration")
    print("x_next: ", x_next, "\n")
    x_previous = x_next