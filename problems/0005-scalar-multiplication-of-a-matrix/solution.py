def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here
	scalar_matrix = []
	for i in range(len(matrix)):
		lst = []
		for el in range(len(matrix[0])):
			lst.append(matrix[i][el] * scalar)
		scalar_matrix.append(lst)
	return scalar_matrix
