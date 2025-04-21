from collections import Counter
s = input().lower()
c = Counter(s.split())
print(c.most_common(1))
