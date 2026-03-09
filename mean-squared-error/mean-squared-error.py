import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    y_pred = np.array(y_pred)
    y_true = np.array(y_true)
    result = (np.sum((y_pred - y_true)**2))/len(y_pred)
    return result