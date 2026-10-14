def orthogonal_projection(v, L):
	# сначала сделаем скалярное произведение
	scalar_multi = 0
	for i in range(len(v)):
		scalar_multi += v[i] * L[i]
	# найдём длину вектора L
	lenght_L = 0
	for i in range(len(v)):
		lenght_L += L[i] ** 2
	# найдём кооэффициент увеличения проекции вектора
	projection = scalar_multi / lenght_L
	# умножим этот коэффициент на вектор L:
	new_L = []
	for i in range(len(v)):
		new_L.append(projection * L[i])
	return new_L