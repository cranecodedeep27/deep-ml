import numpy as np
def make_diagonal(x):
	matrix = []
	for i in range(len(x)):
		lst = []
		p = 0
		if i > 0:
			while p != i:
				lst.append(0)
				p += 1
		if i == p:
			lst.append(x[i])
		p = len(x) - i - 1
		while p != 0:
			lst.append(0)
			p -= 1
		matrix.append(lst)
	return np.array(matrix)