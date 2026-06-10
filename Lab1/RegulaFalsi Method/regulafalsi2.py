import math

def f(x):
    return (x * (math.e ** x) - 2)

x1 = float(input("Enter the number: "))
x2 = float(input("Enter another number: "))
e = float(input("Enter tolerance error: "))
ite = 0

if f(x1) * f(x2) > 0:
    print("Wrong initial guess")
else:
    while True:
        x = (x2 * f(x1) - x1 * f(x2)) / (f(x1) - f(x2))
        ite += 1

        if abs(f(x)) < e:                  # ✅ removed unreliable f(x)==0 check
            print(f"Root is {x:.6f} after {ite} iterations")
            break

        if f(x1) * f(x) < 0:              # ✅ root is between x1 and x
            x2 = x
        else:                              # ✅ root is between x and x2
            x1 = x