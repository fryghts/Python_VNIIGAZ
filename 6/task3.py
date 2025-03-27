before_zero=True
c=0
while (s:=input()).isdecimal():
    s=int(s)
    if s==0:
        before_zero=False
    if before_zero:
        c+=1
