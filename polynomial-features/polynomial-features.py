def polynomial_features(values, degree):
    """
    Generate polynomial features for each value up to the given degree.
    """
    result = []
    for j in range(len(values)):
        l = []
        for i in range(degree + 1):
            l.append(values[j]**i)

        result.append(l)

    return result