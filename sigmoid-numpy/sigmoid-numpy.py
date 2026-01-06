import numpy as np

def sigmoid(*x):
    x = np.asarray(x, dtype=np.float64)
    return 1/(1 + np.exp(-x))