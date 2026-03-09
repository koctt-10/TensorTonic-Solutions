import math

def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    w = (max(values) - min(values))/num_bins
    result = []
    for i in range(len(values)):
        if w == 0:
            w = 0.000001
        result.append(int(min((values[i] - min(values))/w, num_bins - 1)))
    return result