import math

def binary_focal_loss(predictions, targets, alpha, gamma):
    """
    Compute the mean binary focal loss.
    """
    fl = 0
    p_t = [predictions[i] if targets[i] == 1 else 1 - predictions[i] for i in range(len(targets))]
    for i in range(len(p_t)):
        fl += -1 * alpha * ((1 - p_t[i])**gamma) * math.log(p_t[i])
    result = fl/len(p_t)
    return result
