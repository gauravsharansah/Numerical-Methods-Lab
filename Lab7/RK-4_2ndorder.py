def f(x,y,z):
    return z
    
def g(x,y,z):
    return (x*z*z)-(y*y)    # y'' = x*(y')^2 - y^2

def rk4_2nd(x,y,z,h,xp):
    i=0
    print(f"Initial values: x = {x:.3f}, y = {y:.6f}, z = {z:.6f}")
    while(x<xp):
        k1 = h * f(x, y, z)
        l1 = h * g(x, y, z)
        k2 = h * f(x + h/2, y + k1/2, z + l1/2)
        l2 = h * g(x + h/2, y + k1/2, z + l1/2)
        k3 = h * f(x + h/2, y + k2/2, z + l2/2)
        l3 = h * g(x + h/2, y + k2/2, z + l2/2)
        k4 = h * f(x + h, y + k3, z + l3)
        l4 = h * g(x + h, y + k3, z + l3)

        y = y + (k1 + 2*k2 + 2*k3 + k4) / 6
        x = x + h
        z = z + (l1 + 2*l2 + 2*l3 + l4) / 6
        i+=1
        print(f"Step {i}: x = {x:.3f}, y = {y:.6f}, z = {z:.6f}")

def main():
    x0 = float(input("Enter the value of x0: "))
    y0 = float(input("Enter the value of y0: "))
    z0 = float(input("Enter the value of z0: "))
    h = float(input("Enter the value of h: "))
    x = float(input("Enter the value of x: "))
    rk4_2nd(x0, y0, z0, h, x)

if __name__ == "__main__":
    main()
