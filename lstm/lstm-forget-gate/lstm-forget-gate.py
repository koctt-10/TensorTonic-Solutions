import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-np.clip(x, -500, 500)))

def forget_gate(h_prev: np.ndarray, x_t: np.ndarray,
                W_f: np.ndarray, b_f: np.ndarray) -> np.ndarray:
    """Compute forget gate: f_t = sigmoid(W_f @ [h, x] + b_f)"""
    h_prev = np.array(h_prev)
    x_t = np.array(x_t)
    W_f = np.array(W_f)
    b_f = np.array(b_f)
    cont = np.concatenate([h_prev, x_t], axis=-1)
    f_t = sigmoid(cont @ W_f.T + b_f) 
    return f_t