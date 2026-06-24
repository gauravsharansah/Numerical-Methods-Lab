import numpy as np
def leastsq(n,x,y):
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_x2 = np.sum(x**2)
    sum_x3 = np.sum(x**3)
    sum_x4 = np.sum(x**4)
    sum_x5 = np.sum(x**5)
    sum_x6 = np.sum(x**6)
    sum_xy = np.sum(x * y)
    sum_x2y = np.sum((x**2) * y)
    sum_x3y = np.sum((x**3) * y)
    M = np.array([
        [sum_x6, sum_x5, sum_x4, sum_x3],
        [sum_x5, sum_x4, sum_x3, sum_x2],
        [sum_x4, sum_x3, sum_x2, sum_x],
        [sum_x3, sum_x2, sum_x,   n]
    ])
    V = np.array([sum_x3y, sum_x2y, sum_xy, sum_y])
    a, b, c, d = np.linalg.solve(M, V)
    print(f"The required equation is: y = {a:.3f}x^3 + {b:.3f}x^2 + {c:.3f}x + {d:.3f}")

def main():
    n = int(input("Enter the no of the data points: "))
    x = np.zeros(n)
    y = np.zeros(n)

    print("Enter x coordinates of data points: ")
    for i in range(n):
        x[i] = int(input(f"{i+1}: "))

    print("Enter y coordinates of data points: ")
    for i in range(n):
        y[i] = int(input(f"{i+1}: "))

    leastsq(n,x,y)


if __name__ == "__main__":
    main()