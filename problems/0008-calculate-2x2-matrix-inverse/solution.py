def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    g = matrix[0][0] * matrix[1][1]
    p = matrix[0][1] * matrix[1][0]
    det = g - p
    if det == 0:
        return None
    else:
        det1 = 1/det
        a = matrix[1][1] * det1
        b = -1*matrix[0][1] * det1
        c = -1*matrix[1][0] * det1
        d = matrix[0][0] * det1
        A_inv = [[a, b], [c, d]]
    return A_inv