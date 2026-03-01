def percent_change(series):
    result = []
    try:
        for i in range(len(series) - 1):
            result.append((series[i+1] - series[i])/series[i])
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        result = [ 0, 1 ]

    return result