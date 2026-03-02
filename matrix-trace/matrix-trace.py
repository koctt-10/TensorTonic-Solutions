import numpy as np

def matrix_trace(A):
    trace = 0
    elem = 0
    for i in range(len(A)):
        trace += A[i][elem]
        elem += 1
    return trace