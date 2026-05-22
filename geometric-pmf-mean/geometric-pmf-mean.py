import numpy as np

def geometric_pmf_mean(k, p):
    """
    Compute Geometric PMF and Mean.
    """
    e_x = 1/p
    k = np.array(k)
    p_k = (1-p)**(k-1) * p 
    return p_k, e_x