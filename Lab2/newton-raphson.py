import math
def f(x):
    # return (x**2)-(3*x)+2
    return (3*x - math.cos(x) - 1)
def g(x):
    # return 2*x - 3
    return (3 + math.sin(x))

t=0
x0=float(input("Enter the initial guess: "))
e=float(input("Enter tolerance error: "))
n=int(input("Enter maximum steps: "))
ite = 0

if(g(x0)==0):
    t=1
    print("Mathematical error")
else:
    while (ite<n):
        x=x0-f(x0)/g(x0)
        ite+=1
        if(abs(f(x))<e):
            print(f"Root is {x} after {ite} iterations")
            t=1
            break
        x0=x
if (t==0):
    if(n>10):
        print("Root is not convergence.")
    else:
        print("Either root is not convergence or insufficient steps")
