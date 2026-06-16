import numpy as np


def four_parameter_logistic(x, bottom, top, ic50, hill_slope):
    """Four-parameter logistic dose-response function."""
    x = np.asarray(x, dtype=float)
    return bottom + (top - bottom) / (1 + (x / ic50) ** hill_slope)


def safe_mean(values):
    arr = np.asarray(values, dtype=float)
    return float(np.nanmean(arr)) if arr.size else float("nan")
