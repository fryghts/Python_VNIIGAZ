counter = 0
while (s:=input()).isdecimal():
    s = int(s)
    if s == 0:
        counter += 1

print(counter)
