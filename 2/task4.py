n = int(input('Кол-во минут: '))

h = n // 60 % 24
m = n % 60

print(h,':',m,sep='')
