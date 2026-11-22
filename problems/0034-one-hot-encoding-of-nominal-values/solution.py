import numpy as np

def to_categorical(x, n_col=None):
    # Your code here
    if n_col == None:
        n_col = max(x) + 1

    X = np.zeros((len(x), n_col))
    max_len_row = x.max()

    for row_idx, category in enumerate(x):
        row_X = np.zeros(n_col)
        row_X[category] = 1
        X[row_idx] = row_X
    return X
        