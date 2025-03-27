F0 = 0
F1 = 1
n = int(input())

print(F0)
if n >= 1:
    print(F1)

for i in range(2,n+1):
    F = F0 + F1
    print(F)
    F0 = F1
    F1 = F
