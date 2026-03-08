import numpy as np

def leaky_relu(x, alpha=0.01):
    """
    Vectorized Leaky ReLU implementation.
    """
    x = np.array(x)
    result = []
    for i in range(len(x)):
        if x[i] >= 0:
            result.append(x[i])
        else:
            result.append(alpha * x[i])
    result = np.array(result)
    return result