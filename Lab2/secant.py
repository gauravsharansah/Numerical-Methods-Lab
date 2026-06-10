import math
def f(x):
    return (x**3)-(2*x)-5
    # return (3*x + math.sin(x) - math.exp(x))
t=0
x1=float(input("Enter the number: "))
x2=float(input("Enter another number: "))
e=float(input("Enter tolerance error: "))
n=int(input("Enter maximum steps: "))
ite = 0

if (f(x1)*f(x2))>0:
    print("Wrong initial guess")
else:
    while (ite<n and f(x1)!=f(x2)):
        x=(x2*f(x1)-x1*f(x2))/(f(x1)-f(x2))
        ite+=1
        if(abs(f(x))<e):
            print(f"Root is {x} after {ite} iterations")
            t=1
            break
        x1=x2
        x2=x
    if ((f(x1)==f(x2)) and t==0):
        print("Method fails.")
