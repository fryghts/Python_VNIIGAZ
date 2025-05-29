def is_prime(num):
    if num % 2 == 0 and num != 2:
        return False
    for i in range(3,int(num**0.5),2):
        if num % i == 0:
            return False
    return True

for i in range(1,26):
    print(f'{i}: {is_prime(i)}')
    
