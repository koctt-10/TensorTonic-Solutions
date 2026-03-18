import numpy as np

def bernoulli_pmf_and_moments(x, p):
    """
    Compute Bernoulli PMF and distribution moments.
    """
    pmf = []
    for i in range(len(x)):
        if x[i] == 1:
            pmf.append(p)
        else:
            pmf.append(1 - p)

    mu = p
    var = p*(1-p)
    pmf = np.array(pmf)
    return pmf, mu, var