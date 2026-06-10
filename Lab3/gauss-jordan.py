import numpy as np
def mat(n):
    aug = np.zeros((n, n+1))
    for i in range(n):
        print(f"Enter the elements of row {i+1}: ")
        for j in range(n+1):
            aug[i][j] = float(input(f"Enter the value of a[{i}][{j}]: "))
    return aug

def gauss(aug):
    n = len(aug)
    for i in range(n):
        aug[i] = aug[i] / aug[i][i]
        for j in range(n):
            if i!=j:
                aug[j] = aug[j] - aug[i] * aug[j][i]
    x = np.zeros((1,n))
    for i in range(n):
        x[0][i] = aug[i][3]
    return aug, x

order = int(input("Enter the number of variables: "))
a = mat(order)
print(f"The augmented matrix is: \n{a}")

aug, ans = gauss(a)
print(f"The reduced row echelon form is: \n{aug}")
print(f"The solution is: \n{ans}")