import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-np.clip(x, -500, 500)))

def lstm_cell(x_t: np.ndarray, h_prev: np.ndarray, C_prev: np.ndarray,
              W_f: np.ndarray, W_i: np.ndarray, W_c: np.ndarray, W_o: np.ndarray,
              b_f: np.ndarray, b_i: np.ndarray, b_c: np.ndarray, b_o: np.ndarray) -> tuple:
    """Complete LSTM cell forward pass."""
    x_t = np.array(x_t)
    h_prev = np.array(h_prev)
    C_prev = np.array(C_prev)
    W_f = np.array(W_f)
    W_i = np.array(W_i)
    W_c = np.array(W_c)
    W_o = np.array(W_o)
    b_f = np.array(b_f)
    b_i = np.array(b_i)
    b_c = np.array(b_c)
    b_o = np.array(b_o)

    cont = np.concatenate([h_prev, x_t], axis=-1)
    f_t = sigmoid(cont @ W_f.T + b_f)
    i_t = sigmoid(cont @ W_i.T + b_i)
    o_t = sigmoid(cont @ W_o.T + b_o)
    c_hat = np.tanh(cont @ W_c.T + b_c)
    c_t = f_t * C_prev + i_t * c_hat
    h_t = o_t * np.tanh(c_t)

    return h_t, c_t