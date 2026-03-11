def detect_drift(reference_counts, production_counts, threshold):
    """
    Compare reference and production distributions to detect data drift.
    """
    p = [reference_counts[i] / sum(reference_counts) for i in range(len(reference_counts))]
    q = [production_counts[i] / sum(production_counts) for i in range(len(production_counts))]
    result = sum([abs(p[i] - q[i]) for i in range(len(p))])/2
    drift_detected = False
    if result > threshold:
        drift_detected = True
    result = {'score': result, 'drift_detected': drift_detected}
    return result 
