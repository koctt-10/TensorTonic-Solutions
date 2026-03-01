def color_to_grayscale(image):
    result = []
    result_gen = []
    for h in range(len(image)):
        result = []
        for i in range(len(image[h])):
            result.append(0.299 * image[h][i][0] + 0.587 * image[h][i][1] + 0.114 * image[h][i][2])
        result_gen.append(result)

    return result_gen