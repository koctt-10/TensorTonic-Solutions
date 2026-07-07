def generate_anchors(feature_size, image_size, scales, aspect_ratios):
    """
    Generate anchor boxes for object detection.
    """
    anchors = []

    for i in range(feature_size):
        for j in range(feature_size):
            stride = image_size / feature_size
            cx = (j + 0.5) * stride
            cy = (i + 0.5) * stride

            for s in scales:
                for r in aspect_ratios:
                    sqrt_r = r ** 0.5
                    w = s * sqrt_r
                    h = s / sqrt_r

                    x1 = cx - w / 2.0
                    y1 = cy - h / 2.0
                    x2 = cx + w / 2.0
                    y2 = cy + h / 2.0

                    anchors.append([x1, y1, x2, y2])

    return anchors