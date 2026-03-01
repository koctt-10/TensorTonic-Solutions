def differencing(series, order):
    result = []
    result_ex = []
    def one_diff(series:list) -> list:
        result = []
        for i in range(len(series)-1):
            result.append(series[i+1] - series[i])
        return result
    
    for _ in range(order):   
        series = one_diff(series)

    return series