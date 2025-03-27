A = int(input())
B = int(input())

i = A
if A < B:
    while i <= B:
        print(i)
        i += 1
else:
    while i >= B:
        print(i)
        i -= 1

print()
if A < B:
    for i in range(A, B+1):
        print(i)
else:
    for i in range(A, B-1, -1):
        print(i)
