

def ngaussel(A, b):
    import numpy as np
    n = len(b)
    x = np.zeros((n, 1))
    augm = np.column_stack((A, b))
    m = range(0, n-1)
    for k in range(n):
        for i in range(k+1, n):
            m = A[i][k]/A[k][k]
            for j in range(n):
                A[i][j] = A[i][j] - m*A[k][j]
            b[i] = b[i] - m*b[k]

    print(A)

    print(b)

    x[n-1] = b[n-1]/A[n-1][n-1]
    for i in range(n-2, -1, -1):
        S = b[i]
        for j in range(n-1, i, -1):
            S = S - A[i][j]*x[j]
        x[i] = S/A[i][i]

    print(x)
