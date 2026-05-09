import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-np.clip(x, -500, 500)))

def input_gate(h_prev: np.ndarray, x_t: np.ndarray,
               W_i: np.ndarray, b_i: np.ndarray,
               W_c: np.ndarray, b_c: np.ndarray) -> tuple:
    """Compute input gate and candidate memory."""
    h_prev = np.array(h_prev)
    x_t = np.array(x_t)
    W_i = np.array(W_i)
    b_i = np.array(b_i)
    W_c = np.array(W_c)
    b_c = np.array(b_c)
    cont = np.concatenate([h_prev, x_t], axis=-1)
    i_t = sigmoid(cont @ W_i.T + b_i)
    c_t = np.tanh(cont @ W_c.T + b_c)
    return i_t, c_t