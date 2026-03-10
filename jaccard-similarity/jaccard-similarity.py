def jaccard_similarity(set_a, set_b):
    """
    Compute the Jaccard similarity between two item sets.
    """
    count = 0

    set_a = list(set(set_a))
    set_b = list(set(set_b))
    general = set_b
    for i in range(len(set_a)):
        for j in range(len(set_b)):
            if set_a[i] == set_b[j]:
                count += 1
            if set_a[i] in general:
                pass
            else: general.append(set_a[i])
            
    if len(general) == 0:
        return 0
    return count/len(general)
