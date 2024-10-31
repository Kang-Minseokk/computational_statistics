import math


def app_cos(x, sig_num):
    result = 0
    i = 0
    true_value = math.cos(x)
    # 종료 조건 생성
    es = 0.5 * 10 ** (2 - sig_num)
    old_result = 0

    while True:
        result += ((-1) ** i * x ** (2 * i) /
                   math.factorial(2 * i))
        print(f"{i + 1}th Iteration: {result}")

        # 오차 계산
        true_relative_error = (abs(result - true_value) /
                               true_value * 100)
        print(f"True Relative Error: {true_relative_error}%")

        approximate_relative_error = (abs(result - old_result) /
                                      result * 100)
        print(f"Approximate Relative Error: "
              f"{approximate_relative_error}%\n")
        old_result = result

        if es > true_relative_error:
            print(f"{result} {i + 1}th Iteration에서 종료됩니다.")
            break
        i += 1


print(f"True Value : {math.cos(math.pi / 3)}\n")
app_cos(math.pi / 3, 3)
