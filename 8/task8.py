def kredit(S, Q, P):
    c = 0
    while S > P:
        S = (S + S*Q/100) - P
        c += 1
    return c, S
