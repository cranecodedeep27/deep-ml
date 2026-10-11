def transform_basis(B: list[list[int]], C: list[list[int]]) -> list[list[float]]:
    n = len(C)
    
    matrix_C_back = []
    if n == 2:
        det_C = C[0][0] * C[1][1] - C[0][1] * C[1][0]
        lst = []
        lst.append(C[1][1] / det_C)
        lst.append(-C[0][1] / det_C)
        matrix_C_back.append(lst)
        lst = []
        lst.append(-C[1][0] / det_C)
        lst.append(C[0][0] / det_C)
        matrix_C_back.append(lst)
        P = []
        for i in range(n):
            lst = []
            for j in range(n):
                summ = 0
                for k in range(n):
                    summ += matrix_C_back[i][k] * B[k][j]
                lst.append(summ)
            P.append(lst)

    elif n == 3:
        matrix_adds = []
        for i in range(3):
            lst = []
            for j in range(3):
                minor = []
                for r in range(3):
                    if r == i:
                        continue
                    row =[]
                    for c in range(3):
                        if c == j:
                            continue
                        row.append(C[r][c])
                    minor.append(row)
                det = minor[0][0] * minor[1][1] - minor[0][1] * minor[1][0]
                if (j+i) % 2 == 1:
                    lst.append(-det)
                else:
                    lst.append(det)
            matrix_adds.append(lst)
        det_C = (
            C[0][0] * matrix_adds[0][0]
            + C[0][1] * matrix_adds[0][1]
            + C[0][2] * matrix_adds[0][2]
        )
        for i in range(n):
            lst = []
            for j in range(n):
                lst.append(1/det_C * matrix_adds[j][i])
            matrix_C_back.append(lst)
        P = []
        for i in range(n):
            lst = []
            for j in range(n):
                summ = 0
                for k in range(n):
                    summ += matrix_C_back[i][k] * B[k][j]
                lst.append(summ)
            P.append(lst)
    return P
