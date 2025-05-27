class NegativeError(Exception):
    pass

def get_a_num():
    a = int(input())
    if a <= 0:
        raise NegativeError('get_a_num failed')
    return a

while True:
    try:
        print(100/get_a_num())
        break
    except ValueError:
        print('Неверный ввод')
    except NegativeError as err:
        print('Отрицательный ввод')
        print(err)

print('END')
