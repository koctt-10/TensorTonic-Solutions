import numpy as np

def vector_norm_3d(v):
    arr = np.asarray(v)
    if arr.ndim == 1:
        return np.linalg.norm(arr)
    else:
        return np.linalg.norm(arr, axis=1)