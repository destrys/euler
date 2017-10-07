import math

def answer(n):
    return natural_3and5(n)


def natural_3and5_brute(upper=1000):
    output = 0
    for i in range(1,upper):
        if i % 3 == 0:
            output += i
            continue
        if i % 5 == 0:
            output += i
            continue
    return output


def natural_3and5(n=1000):
    floor3 = math.floor((n-1)/3)
    floor5 = math.floor((n-1)/5)
    floor15 = math.floor((n-1)/15)
    term1 = 3 * (floor3 * (floor3 + 1)) / 2
    term2 = 5 * (floor5 * (floor5 + 1)) / 2
    term3 = 15 * (floor15 * (floor15 + 1)) / 2
    output = term1 + term2 + term3
    return output

def natural_3and5_lambda(n=1000):
    f = lambda x: math.floor((n - 1) / x)
    t = lambda x: x * (f(x) * (f(x) + 1)) / 2
    output = t(3) + t(5) - t(15)
    return output
