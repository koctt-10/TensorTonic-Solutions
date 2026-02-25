import numpy as np

def matrix_transpose(A):
    trans_matrix = np.array([[0 for i in range(len(A))] for j in range(len(A[0]))])
    for j in range(len(A)):
        for i in range(len(A[0])):
            trans_matrix[i][j] = A[j][i]
    return trans_matrix