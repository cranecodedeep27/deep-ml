def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    g = matrix[0][0] * matrix[1][1]
    p = matrix[0][1] * matrix[1][0]
    det = g - p
    if det == 0:
        return None
    det_inv = 1/det
    a = matrix[1][1] * det_inv
    b = -matrix[0][1] * det_inv
    c = -matrix[1][0] * det_inv
    d = matrix[0][0] * det_inv
    A_inv = [[a, b], [c, d]]
    return A_inv