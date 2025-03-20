a = int(input())

if a >= 0:
    print('Positive')
elif a > -100:
    print('-100<',a,'<0')
elif a > -100000:
    print('-100000<',a,'<-100')
else:
    print(a,'<-100000')
