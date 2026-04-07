import math

def ndcg(relevance_scores, k):
    """
    Compute NDCG@k.
    """
    if k > len(relevance_scores):
        DCG = sum([(2**relevance_scores[i]-1)/(math.log((i+2), 2)) for i in range(len(relevance_scores))])
        relevance_scores = sorted(relevance_scores, reverse=True)
        IDCG = sum([(2**relevance_scores[i]-1)/(math.log((i+2), 2)) for i in range(len(relevance_scores))])
    else:
        DCG = sum([(2**relevance_scores[i]-1)/(math.log((i+2), 2)) for i in range(k)])
        relevance_scores = sorted(relevance_scores, reverse=True)
        IDCG = sum([(2**relevance_scores[i]-1)/(math.log((i+2), 2)) for i in range(k)])
    if IDCG == 0:
        IDCG = 1
    return DCG/IDCG