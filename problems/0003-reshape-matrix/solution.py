def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	elements = []
	for rows in a:
		for value in rows:
			elements.append(value)

	rows, cols = new_shape

	if rows * cols != len(elements):
		return []
	else:
		resheped_matrix = []
		k = 0
		for i in range(rows):
			lst = []
			for j in range(cols):
				lst.append(elements[k])
				k += 1
			resheped_matrix.append(lst)
	return resheped_matrix


	
	