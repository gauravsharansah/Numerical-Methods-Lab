import math
def f(x):
    return 4 * math.sin(x) - math.e**x

x1=float(input("Enter the number: "))
x2=float(input("Enter another number: "))
e=float(input("Enter tolerance error: "))
ite = 0

if (f(x1)*f(x2))>0:
    print("Wrong initial guess")
else:
    while True:
        x=(x1+x2)/2
        ite+=1
        if abs(f(x))<e:
            print(f"Root is {x} after {ite} iterations")
            break
        if (f(x1)*f(x))>0:
            x1=x
        else:
            x2=x
