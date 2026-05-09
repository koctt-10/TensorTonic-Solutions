import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-np.clip(x, -500, 500)))

def output_gate(h_prev: np.ndarray, x_t: np.ndarray, C_t: np.ndarray,
                W_o: np.ndarray, b_o: np.ndarray) -> tuple:
    """Compute output gate and hidden state."""
    h_prev = np.array(h_prev)
    x_t = np.array(x_t)
    C_t = np.array(C_t)
    W_o = np.array(W_o)
    b_o = np.array(b_o)
    cont = np.concatenate([h_prev, x_t], axis=-1)
    o_t = sigmoid(cont @ W_o.T + b_o)
    h_t = o_t * np.tanh(C_t)

    return o_t, h_t