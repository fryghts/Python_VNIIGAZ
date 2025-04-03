def divides(a, b):
    if a % b == 0:
        return a / b
    if b % a == 0:
        return b / a
    return 0
