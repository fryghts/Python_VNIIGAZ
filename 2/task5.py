n = int(input())

n3 = n % 10
n2 = n // 10 % 10
n1 = n // 100

print(n1,'+',n2,'+',n3,'=',n1+n2+n3)
