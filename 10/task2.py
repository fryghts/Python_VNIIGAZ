S = [1,5,-2,3,9,0,1,2]
S1 = []
count=0
for idx in range(1,len(S)-1):
    if (S[idx]>S[idx-1]) & (S[idx]>S[idx+1]):
        count+=1
        S1.append(S[idx])
print(count)
