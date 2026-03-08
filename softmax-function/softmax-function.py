import numpy as np

def softmax(x):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
    """
    x = np.array(x)
    x = x - np.max(x,keepdims=True)
    if x.ndim == 2:
        result = []
        for i in range(len(x)):
            result.append(np.exp(x[i])/np.sum(np.exp(x[i])))
    else:   
        result = np.exp(x)/np.sum(np.exp(x))
    return result