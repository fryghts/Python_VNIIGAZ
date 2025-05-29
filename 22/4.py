a = list(map(int,input().split()))

#a = [1,2,3] -> [2,3,1]

def fun(s):
    s.append(s.pop(0))

def fun2(s):
    return s[1:]+[s[0]]
