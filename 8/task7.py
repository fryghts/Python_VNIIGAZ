def vklad(P, X, N):
    for i in range(N):
        X += X * P / 100
    return X

print(vklad(20, 1000000, 5))
