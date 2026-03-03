import numpy as np

def angle_between_3d(v, w):
    v = np.array(v)
    w = np.array(w)
    mul = np.sum(v*w)
    mul_len = np.sqrt(np.sum(v**2)) * np.sqrt(np.sum(w**2))
    arr = mul / mul_len
    cos = np.clip(arr, -1, 1)
    result = np.arccos(cos)
    return result