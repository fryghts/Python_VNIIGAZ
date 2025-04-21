def angle(alpha):
    #360/12=30
    #360/12/60=0.5
    #360/12/60/60=0.5/60
    #
    H = alpha // 30
    M = alpha % 30 // 0.5
    S = alpha % 30 % 0.5 // (0.5/60)
    return H, M, S
