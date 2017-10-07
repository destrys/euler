
def natural3and5Brute(upper=1000):
    output = 0
    for i in range(1,upper):
        if i % 3 == 0:
            output += i
            continue
        if i % 5 == 0:
            output += i
            continue
    return output

def answer(n):
    return natural3and5Brute(n)
