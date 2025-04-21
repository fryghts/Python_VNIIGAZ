for idx in range(0,len(S),2):
    print(S[idx])

for elem in S[::2]:
    print(elem)

for elem in S:
    if elem % 2 == 0:
        print(elem)

for idx in range(1,len(S)):
    if S[idx] > S[idx-1]:
        print(S[idx])
