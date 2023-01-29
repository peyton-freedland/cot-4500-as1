from __init__ import *
# Base function for questions 1-3
def double_precision():
    sign = 0
    exponent = 10000000111
    exp, i = 0, 0
    while(exponent != 0):
        exp += (exponent % 10) * pow(2, i)
        exponent //= 10
        i += 1

    fraction = str(111010111001000000000000000000000000000000)
    f = 0
    i = 1
    for item in fraction:
        f += int(item) * (0.5 ** i)
        i += 1
    
    # Question 1
    num = ((-1) ** sign) * (2 ** (exp - 1023)) * (1 + f)
    ans1 = num
    print("{:.5f}".format(num))
    print()

    # Question 2
    num *= (10 ** -3)
    num = math.floor(num * 1000) / 1000
    num *= 1000
    print(num)
    print()

    # Question 3
    num += 0.500
    print(round(num, ndigits = 0))
    print()

    # Question 4
    def absolute_error(precise: float, approx: float):
        return abs(precise - approx)
    
    def relative_error(precise: float, approx: float):
        return abs(absolute_error(precise, approx)) / abs(precise)

    print(absolute_error(ans1, round(ans1, 0)))
    print("{:.31f}".format(relative_error(ans1, round(ans1, 0))))
    print()

# Question 5
def question_5():
    def series(x, k: int):
        return((-1) ** k) * ((x ** k) / (k ** 3))
    min_error = 1e-4
    current_iteration = 1
    while(abs(series(1, current_iteration)) > min_error):
        current_iteration += 1
    print(current_iteration - 1)
    print()
    return

# Question 6
def question_6():
    def bisection_method(f, a, b, accuracy):
        if np.sign(f(a)) == np.sign(f(b)):
            raise Exception("The scalars a and b do not bound a root")
        midpoint = (a + b) / 2
        if np.abs(a - b) <= accuracy:
            return 0
        elif np.sign(f(a)) == np.sign(f(midpoint)):
            return bisection_method(f, midpoint, b, accuracy) + 1
        elif np.sign(f(b)) == np.sign(f(midpoint)):
            return bisection_method(f, a, midpoint, accuracy) + 1

    def newton_raphson_method(f, df, initial, accuracy):
        result = f(initial) / df(initial)
        x = initial
        count = 1
        while(abs(result) >= accuracy):
            x -= result
            count += 1
            result = f(x) / df(x)
        return count
    f_x = lambda x: (x ** 3) + (4 * (x ** 2)) - 10
    df_dx = lambda x: 3 * (x ** 2) + (8 * x)
    print(bisection_method(f_x, -4, 7, 0.0001))
    print()
    print(newton_raphson_method(f_x, df_dx, 7, 0.0001))
    print()

double_precision()
question_5()
question_6()