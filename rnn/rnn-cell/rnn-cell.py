import numpy as np

def rnn_cell(x_t: np.ndarray, h_prev: np.ndarray, 
             W_xh: np.ndarray, W_hh: np.ndarray, b_h: np.ndarray) -> np.ndarray:
    """
    Single RNN cell forward pass.
    """
    x_t = np.array(x_t)
    h_prev = np.array(h_prev)
    W_xh = np.array(W_xh)
    W_hh = np.array(W_hh)
    b_h = np.array(b_h)
    result = np.tanh(np.dot(x_t, W_xh.T) + np.dot(h_prev, W_hh.T) + b_h)

    return result