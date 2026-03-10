def he_initialization(W, fan_in):
    """
    Scale raw weights to He uniform initialization.
    """
    l = (6/fan_in)**0.5
    for i in range(len(W)):
        for j in range(len(W[i])):
            W[i][j] = W[i][j] * 2 * l -l

    return W