import numpy as np

def batch_norm_forward(x, gamma, beta, eps=1e-5):
    """
    Forward-only BatchNorm for (N,D) or (N,C,H,W).
    """
    x = np.array(x)
    g = np.array(gamma)
    b = np.array(beta)
    if x.ndim == 2:
        axis = 0
    elif x.ndim == 4:
        axis = (0, 2, 3)
    else:
        raise ValueError()
    mu = np.mean(x, axis=axis, keepdims=True)
    sig = np.var(x, axis=axis, keepdims=True)
    x_norm = (x - mu) / np.sqrt(sig + eps)
    if x.ndim == 4:
        g = g.reshape(1, -1, 1, 1)
        b = b.reshape(1, -1, 1, 1)

    result = g*x_norm + b
    return result