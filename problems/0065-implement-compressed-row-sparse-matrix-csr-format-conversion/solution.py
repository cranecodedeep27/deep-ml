import numpy as np

def compressed_row_sparse_matrix(dense_matrix: list[list[int|float]]) -> list:
	vals = []
	col_idx = []
	row_ptr = [0]
	cum_sum = 0
	count_columns = len(dense_matrix)
	for i in range(len(dense_matrix)):
		for j in range(count_columns):
			if dense_matrix[i][j] != 0:
				vals.append(dense_matrix[i][j])
				col_idx.append(j)
		row_ptr.append(len(vals))
	return vals, col_idx, row_ptr

