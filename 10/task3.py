S = [1,5,-2,3,9,0,1,2]
print(S)
S_max = S[0]
S_idx = 0
for i in range(len(S)):
    if S[i] > S_max:
        S_max = S[i]
        S_idx = i
print(S_max,S_idx)
