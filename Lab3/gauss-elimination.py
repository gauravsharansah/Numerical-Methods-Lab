import numpy as np
def mat(n):
    aug = np.zeros((n, n+1))
    for i in range(n):
        print(f"Enter the elements of row {i+1}: ")
        for j in range(n+1):
            aug[i][j] = float(input(f"Enter the value of a[{i}][{j}]: "))
    return aug

def gauss_pivot(aug):
    n = len(aug)
    max = abs(aug[0][0])
    for i in range(n):
        if abs(aug[i][0]) > max:
            temp = aug[i]
            aug[i] = aug[0]
            aug[0] = temp
            max = abs(aug[0][0])
    for i in range(n):
        for j in range(i+1,n):
            aug[j] = aug[j] - aug[i] * (aug[j][i]/aug[i][i])
    x = np.zeros((1,n))
    for i in range(n-1,-1,-1):
        res = 0
        for j in range(i+1,n):
            res = res + aug[i][j] * x[0][j]
        x[0][i] = (aug[i][n] - res)/aug[i][i]
    return aug, x

num = int(input("Enter the number of variables: "))
a = mat(num)
print(f"The augmented matrix is: \n{a}")

aug, ans = gauss_pivot(a)
print(f"The reduced row echelon form is: \n{aug}")
print(f"The solution is: \n{ans}")
