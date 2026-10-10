def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	lst = []
	if mode == "column":
		for i in range(len(matrix[0])):
			summ = 0
			for j in range(len(matrix)):
				summ += matrix[j][i]
			sum_mean = summ / len(matrix)
			lst.append(sum_mean)
	elif mode == "row":
		for i in range(len(matrix)):
			summ = 0
			for j in range(len(matrix[0])):
				summ += matrix[i][j]
			sum_mean = summ / len(matrix[0])
			lst.append(sum_mean)

	return lst