def remove_stopwords(tokens:list, stopwords:list) -> list:
    """
    Returns: list[str] - tokens with stopwords removed (preserve order)
    """
    result = []
    for i in range(len(tokens)):
        result.append(tokens[i])
        if tokens[i] in stopwords:
            result.pop()

    return result