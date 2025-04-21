S = [1,5,-2,3,9,0,1,2]
print(S)
Max_idx = S.index(max(S))
Min_idx = S.index(min(S))
S[Max_idx], S[Min_idx] = S[Min_idx], S[Max_idx]
print(S)
