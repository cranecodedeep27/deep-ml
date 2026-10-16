import numpy as np

def calculate_dot_product(vec1, vec2):
	scalar_dot = 0
	for i in range(len(vec1)):
		scalar_dot += vec1[i] * vec2[i]
	return scalar_dot