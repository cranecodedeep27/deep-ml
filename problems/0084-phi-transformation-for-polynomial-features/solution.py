import numpy as np

def phi_transform(data: list[float], degree: int) -> list[list[float]]:
	if degree < 0:
		return []
	phi_list = []
	for x in data:
		row = []
		for power in range(degree + 1):
			row.append(float(x ** power))
		phi_list.append(row) 
	return phi_list