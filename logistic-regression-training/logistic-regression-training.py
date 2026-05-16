import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    X = np.atleast_2d(X)
    y = np.asarray(y).ravel()
    
    N, d = X.shape

    w = np.zeros(d)
    b = 0.0
    
    for step in range(steps):
        z = X @ w + b
        p = _sigmoid(z) 
        
        error = p - y
        dw = (X.T @ error) / N
        db = np.mean(error)
        w -= lr * dw
        b -= lr * db
    
    return w, b