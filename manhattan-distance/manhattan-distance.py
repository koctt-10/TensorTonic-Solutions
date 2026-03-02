import numpy as np

def manhattan_distance(x, y):
    x = np.array(x)
    y = np.array(y)
    return int(np.abs(np.sum(abs(x-y))))