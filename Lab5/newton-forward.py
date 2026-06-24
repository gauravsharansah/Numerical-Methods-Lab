import numpy as np
def newton(n,x,y,Xp):
    for j in range (1,n):
        for i in range(n-j):
            y[i][j] = y[i+1][j-1] - y[i][j-1]
    print(f"The value of y matrix is: ")
    for i in range (n):
        for j in range (n):
            print(f"{y[i][j]:.3f}", end="\t")
        print()
    ratio = 1
    yp = y[0][0]
    h = x[1] - x[0]
    p = (Xp - x[0])/h
    for j in range (1,n):
        ratio *= (p-(j-1))/j
        yp = yp + (ratio*y[0][j])
    print(f"The value of y is: {yp:.3f}")

def main():
    n = int(input("Enter the no of the data points: "))
    x = np.zeros(n)
    y = np.zeros((n,n))

    print("Enter x coordinates of data points: ")
    for i in range(n):
        x[i] = float(input(f"{i+1}: "))

    print("Enter y coordinates of data points: ")
    for i in range(n):
        y[i][0] = float(input(f"{i+1}: "))

    Xp = float(input("Enter value of x for which y is needed: "))

    newton(n,x,y,Xp)


if __name__ == "__main__":
    main()