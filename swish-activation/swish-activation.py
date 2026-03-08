import numpy as np

def swish(x):
    """
    Implement Swish activation function.
    """
    x = np.array(x)
    def sigmoid(x):
        return 1 / (1 + np.exp(-x))
    result = x * sigmoid(x)
    return result