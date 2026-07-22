import numpy as np
def P(x, h):
    return (1/(h*h)) - (x/(2*h))

def Q(x, h):
    return (-2/(h*h)) + 1

def R(x, h):
    return (1/(h*h)) + (x/(2*h))

def B(x):
    return (3*x*x) + 2


def fdm_bvp(x0, xn, y0, yn, h):
    n = int(round((xn - x0) / h))
    x = [x0 + i*h for i in range(n + 1)] 

    A = np.zeros((n-1, n-1))
    b = np.zeros(n-1)

    for i in range(1, n):
        p = P(x[i], h)
        q = Q(x[i], h)
        r = R(x[i], h)

        if i != 1:
            A[i-1][i-2] = p
        A[i-1][i-1] = q
        if i != n-1:
            A[i-1][i] = r

        b[i-1] = B(x[i])

    b[0]  -= P(x[1], h) * y0
    b[-1] -= R(x[n-1], h) * yn

    y = np.linalg.solve(A, b)

    print("The solution is: ")
    for i in range(n-1):
        print(f"x = {x[i+1]:.3f}, y = {y[i]:.6f}")


def main():
    x0 = float(input("Enter the value of x0: "))
    y0 = float(input("Enter the value of y0: "))
    xn = float(input("Enter the value of xn: "))
    yn = float(input("Enter the value of yn: "))
    h  = float(input("Enter the value of h: "))
    fdm_bvp(x0, xn, y0, yn, h)


if __name__ == "__main__":
    main()
