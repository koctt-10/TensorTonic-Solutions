import numpy as np

def focal_loss(p, y, gamma=2.0):
    """
    Compute Focal Loss for binary classification.
    """
    p = np.array(p)
    y = np.array(y)
    fl = -((1-p)**gamma)*y*np.log(p) - (p**gamma)*(1-y)*np.log(1-p)

    result = sum(fl)/len(fl)

    return result