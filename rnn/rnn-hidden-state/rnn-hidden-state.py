import numpy as np

def init_hidden(batch_size: int, hidden_dim: int) -> np.ndarray:
    """
    Initialize the hidden state for an RNN.
    """
    den_dim = [0.0 for j in range(hidden_dim)]
    result = []
    for i in range(batch_size):
        result.append(den_dim)
    result = np.array(result)
    return result