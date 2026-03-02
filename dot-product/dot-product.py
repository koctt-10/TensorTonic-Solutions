import numpy as np

def dot_product(x, y):
    x = np.array(x)
    y = np.array(y)
    dot_prod = np.sum(x*y)
            
    return dot_prod