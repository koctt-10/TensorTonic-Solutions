def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    result = []
    for i in range(0,len(tokens),chunk_size-overlap):
        if len(tokens[i:i+chunk_size]) < chunk_size and i != 0:
            break
        else: 
            result.append(tokens[i:i+chunk_size])

    return result