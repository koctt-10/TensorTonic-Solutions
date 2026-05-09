import numpy as np

def update_cell_state(C_prev: np.ndarray, f_t: np.ndarray,
                      i_t: np.ndarray, c_tilde: np.ndarray) -> np.ndarray:
    """Update cell state: C_t = f_t * C_prev + i_t * c_tilde"""
    C_prev = np.array(C_prev)
    f_t = np.array(f_t)
    i_t = np.array(i_t)
    c_tilde = np.array(c_tilde)

    c_t = f_t * C_prev + i_t * c_tilde

    return c_t