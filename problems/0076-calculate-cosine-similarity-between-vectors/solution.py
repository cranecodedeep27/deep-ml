from math import sqrt
import numpy as np

def cosine_similarity(v1, v2):
	scalar_multi = 0
	n = len(v1)
	for i in range(n):
		scalar_multi += v1[i] * v2[i]

	lenght_v1 = 0
	lenght_v2 = 0
	for i in range(n):
		lenght_v1 += v1[i] ** 2
		lenght_v2 += v2[i] ** 2

	lenght_v1 = sqrt(lenght_v1)
	lenght_v2 = sqrt(lenght_v2)
	multi_lenght = lenght_v1 * lenght_v2
	cos_alpha = scalar_multi / multi_lenght
	return cos_alpha
	