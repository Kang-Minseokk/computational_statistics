import math
def app_sin(x, n):
    result = 0
    true_value = math.sin(x)
    for i in range(n):
        # 값 구하기
        result += (-1) ** i * (x ** (2 * i + 1) /
                               math.factorial(2 * i + 1))
        print(f"{i+1}th Iteration Result: {result}")
        # 에러 구하기
        relative_error = ((true_value - result) / true_value)
        print(f"Relative Error: {relative_error}\n")

app_sin(0.9, 7)
