print('y = a1*x + b1')
a1 = int(input('a1: '))
b1 = int(input('b1: '))
print('y = a2*x + b2')
a2 = int(input('a2: '))
b2 = int(input('b2: '))

x = (b2 - b1) / (a1 - a2)
y = a1*x + b1
print('Координаты:',x,y)
