import numpy as np

def clip_gradients(g, max_norm):
    """
    Clip gradients using global norm clipping.
    """
    g = np.array(g)

    if max_norm <= 0:
        return g
        
    grad_norm = np.linalg.norm(g)

    if grad_norm <= max_norm:
        return g
    else:
        return g*(max_norm/grad_norm)