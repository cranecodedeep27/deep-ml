import numpy as np

def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
    # Your code here
    standardized_data = np.zeros(data.shape)

    for j in range(data.shape[1]):
        column = data[:, j]
        mean_val = data[:, j].mean()
        std_val = data[:, j].std()
        X_new_standard = ((column - mean_val) / std_val).round(4)
        standardized_data[:, j] = X_new_standard

    normalized_data = np.zeros_like(standardized_data)
    for i in range(data.shape[1]):
        column = data[:, i]
        min_val = min(data[:, i])
        max_val = max(data[:, i])
        X_new_normalized = ((column - min_val) / (max_val - min_val)).round(4)
        normalized_data[:, i] = X_new_normalized
    return standardized_data, normalized_data