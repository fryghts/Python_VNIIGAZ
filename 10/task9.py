def binsearch(s, item):
    idx_high = len(s)-1
    idx_low = 0
    idx_mid = idx_high // 2
    if s[idx_high] < item or s[idx_low] > item:
        return False
    if s[idx_high] == item or s[idx_low] == item:
        return True
    while idx_high - idx_low > 1:
        if s[idx_mid] > item:
            idx_high = idx_mid
        elif s[idx_mid] < item:
            idx_low = idx_mid
        else:
            return True
        idx_mid = round((idx_high + idx_low) / 2)
    return False

for i in range(-1, 21):
    print(i, 'YES' if binsearch(range(0,20,2), i) else 'NO')
