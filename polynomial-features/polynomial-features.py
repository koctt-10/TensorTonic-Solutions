def polynomial_features(values, degree):
    result = []
    def one_deg(value):
        value = [value**i for i in range(degree+1)]
        return value

    for j in range(len(values)):
        result.append(one_deg(values[j]))

    return result
