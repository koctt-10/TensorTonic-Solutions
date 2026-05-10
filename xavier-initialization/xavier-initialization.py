def xavier_initialization(W, fan_in, fan_out):
    """
    Scale raw weights to Xavier uniform initialization.
    """
    L = (6/(fan_in + fan_out))**0.5
    W_new = []
    for i in range(len(W)):
        t = W[i]
        W_new.append([t[j]*2*L - L for j in range(len(t))])

    return W_new