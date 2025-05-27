def gen(a):
    S = 0
    for i in range(1, a+1):
        S += 1/i**2
        yield S

