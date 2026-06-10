def matmul(A, B):
    if not A or not B or len(A[0]) != len(B):
        raise ValueError("Incompatible dimensions for matrix multiplication.")

    c = len(B[0])
    C = []
    for i in range(len(A)):
        C.append([0] * c)

    for i in range(len(A)):
        for j in range(c):
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]

    return C

def mat():
    a = int(input("Enter no of rows: "))
    b = int(input("Enter no of columns: "))
    A = []
    for i in range(a):
        A.append([0] * b)
    for i in range(a):
        for j in range(b):
            A[i][j] = int(input("Enter element in row {} and column {}: ".format(i+1, j+1)))
    return A

print("Enter Matrix A:")
A = mat()
print("Enter Matrix B:")
B = mat()
C = matmul(A, B)
print("Matrix is:", A)
print("Matrix is:", B)
print("Result of multiplication is:", C)