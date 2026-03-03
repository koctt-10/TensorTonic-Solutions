import numpy as np

def auc(fpr, tpr):
    fpr = np.array(fpr)
    tpr = np.array(tpr)
    result = np.trapezoid(tpr, fpr)
    return result