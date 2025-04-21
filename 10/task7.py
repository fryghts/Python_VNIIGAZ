from random import randint
N = int(input())
K = ['I']*N
print(''.join(K))

n1, n2 = randint(0, N-1), randint(0, N-1)
if n1 > n2:
    n1,n2 = n2,n1
for i in range(n1,n2+1):
    K[i] = '.'
print(''.join(K))
n1, n2 = randint(0, N-1), randint(0, N-1)
if n1 > n2:
    n1,n2 = n2,n1
for i in range(n1,n2+1):
    K[i] = '.'
print(''.join(K))
