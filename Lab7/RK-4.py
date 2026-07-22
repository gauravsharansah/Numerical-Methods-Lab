def f(x,y):
    return (2*y)/x

def rk4(x,y,h,xp):
    i=0
    print(f"Initial values: x = {x:.3f}, y = {y:.6f}")
    while(x<xp):
        k1 = h * f(x, y)
        k2 = h * f(x + h/2, y + k1/2)
        k3 = h * f(x + h/2, y + k2/2)
        k4 = h * f(x + h, y + k3)

        y = y + (k1 + 2*k2 + 2*k3 + k4) / 6
        x = x + h
        i+=1
        print(f"Step {i}: x = {x:.3f}, y = {y:.6f}")

def main():
    x0 = float(input("Enter the value of x0: "))
    y0 = float(input("Enter the value of y0: "))
    h = float(input("Enter the value of h: "))
    x = float(input("Enter the value of x: "))
    rk4(x0, y0, h, x)

if __name__ == "__main__":
    main()
