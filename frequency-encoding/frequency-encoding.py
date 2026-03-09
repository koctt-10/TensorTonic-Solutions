def frequency_encoding(values):
    """
    Replace each value with its frequency proportion.
    """
    s = len(values)
    result = []
    for i in range(s):
        result.append(values.count(values[i])/s)

    return result