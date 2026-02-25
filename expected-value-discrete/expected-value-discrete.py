import numpy as np

def expected_value_discrete(x, p):
    sum_e = 0
    if sum(p) != 1:
        raise ValueError()
    for i in range(len(x)):
        sum_e = sum_e + x[i]*p[i]
    
    return sum_e