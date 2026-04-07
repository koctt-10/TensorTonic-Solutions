import math

def perplexity(prob_distributions, actual_tokens):
    """
    Compute the perplexity of a token sequence given predicted distributions.
    """
    N = len(actual_tokens)
    total_log_prob = 0.0
    for i, token in enumerate(actual_tokens):
        p = prob_distributions[i][token]
        total_log_prob += math.log(p)

    cross_entropy = -total_log_prob / N
    return math.exp(cross_entropy)