import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    result = []
    for i in range(len(vocab)):
        count = 0
        for j in range(len(tokens)):
            if vocab[i] == tokens[j]:
                count +=1
  
        result.append(count)
    result = np.array(result, dtype = int)
    return result