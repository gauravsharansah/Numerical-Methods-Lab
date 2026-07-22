def f(x, y, z):
    return z

def g(x, y, z):
    return x - 2*z - y     # from y'' + 2*y' + y = x


def rk4_ivp(x, y, z, h, xn, verbose=False):
    n = int(round((xn - x) / h))
    if verbose:
        print(f"Initial values: x = {x:.3f}, y = {y:.6f}, z = {z:.6f}")
    for i in range(n):
        k1 = h * f(x, y, z)
        l1 = h * g(x, y, z)
        k2 = h * f(x + h/2, y + k1/2, z + l1/2)
        l2 = h * g(x + h/2, y + k1/2, z + l1/2)
        k3 = h * f(x + h/2, y + k2/2, z + l2/2)
        l3 = h * g(x + h/2, y + k2/2, z + l2/2)
        k4 = h * f(x + h, y + k3, z + l3)
        l4 = h * g(x + h, y + k3, z + l3)

        y = y + (k1 + 2*k2 + 2*k3 + k4) / 6
        z = z + (l1 + 2*l2 + 2*l3 + l4) / 6
        x = x + h
        if verbose:
            print(f"Step {i+1}: x = {x:.3f}, y = {y:.6f}, z = {z:.6f}")
    return y


def linear_shooting(x, y, xn, yn, h, z1, z2, tol=1e-9):
    Y1 = rk4_ivp(x, y, z1, h, xn)
    print(f"Trial 1: assume z1 = {z1:.6f}  ->  Y1 = y(xn) = {Y1:.6f}")
    if abs(Y1 - yn) < tol:
        print("Y1 already matches yn -- z1 was the correct slope.")
        return z1

    Y2 = rk4_ivp(x, y, z2, h, xn)
    print(f"Trial 2: assume z2 = {z2:.6f}  ->  Y2 = y(xn) = {Y2:.6f}")
    if abs(Y2 - yn) < tol:
        print("Y2 already matches yn -- z2 was the correct slope.")
        return z2
    
    z = z1 + (yn - Y1) * (z2 - z1) / (Y2 - Y1)
    Y3 = rk4_ivp(x, y, z, h, xn)
    print(f"Corrected: z = {z:.6f}  ->  Y3 = y(xn) = {Y3:.6f}")
    return z


def main():
    x0 = float(input("Enter the value of x0: "))
    y0 = float(input("Enter the value of y0: "))
    xn = float(input("Enter the value of xn: "))
    yn = float(input("Enter the value of yn: "))
    h  = float(input("Enter the value of h: "))
    z1 = float(input("Enter first assumed slope z1 = y'(x0): "))
    z2 = float(input("Enter second assumed slope z2 = y'(x0): "))

    z0 = linear_shooting(x0, y0, xn, yn, h, z1, z2)
    rk4_ivp(x0, y0, z0, h, xn,True)


if __name__ == "__main__":
    main()
