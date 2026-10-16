def compressed_col_sparse_matrix(dense_matrix):
	val = []
	row_inx = []
	col_ptr = [0]
	count = 0
	for i in range(len(dense_matrix)):
		for j in range(len(dense_matrix[0])):
			if dense_matrix[j][i] != 0:
				val.append(dense_matrix[j][i])
				row_inx.append(j)
				count += 1
		col_ptr.append(count)

	return val, row_inx, col_ptr
			
