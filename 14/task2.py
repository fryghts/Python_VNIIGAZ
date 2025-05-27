def messages(num):
    last = num % 10
    lastlast = num % 100 // 10
    if (lastlast == 1) or (5 <= last <=9) or (last == 0):
        print(f'У вас {num} новых сообщений')
    elif last == 1:
        print(f'У вас {num} новое сообщение')
    else:
        print(f'У вас {num} новых сообщения')

for i in range(1,100):
    messages(i)
    
