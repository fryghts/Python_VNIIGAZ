def maxfun(S, F1, *F):
    max_val = F1(S)
    max_fun = F1
    for fun in F:
        val = fun(S)
        print(val)
        if val > max_val:
            max_val = val
            max_fun = fun
    return max_fun

def a(S):
    b = 0
    for i in S:
        b+= i*2

        
def a(S):
    b = 0
    for i in S:
        b+= i*2
    return b

def b(S):
    return sum(S)*2

def c(S):
    return max(S)+10

S = [-1,3,10]
F = maxfun(S,a,b,c)
print(F)
