def cross_product(a, b):
    matrix_c = [a, b]
    cx = a[1]*b[2] - a[2]*b[1]
    cy = -(a[0]*b[2]) + a[2]*b[0]
    cz = a[0]*b[1] - a[1]*b[0]
    return [cx, cy, cz]

        

        