from random import randint
x1 = [randint(1,100) for i in range(10)]
x2 = [randint(1,100) for i in range(10)]
x = [elem for elem in x1 if elem in x2]
