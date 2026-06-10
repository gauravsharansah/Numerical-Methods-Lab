def f(x):
    return (x**2)-(x)-2

x1=float(input("Enter the number: "))
x2=float(input("Enter another number: "))
e=float(input("Enter tolerance error: "))
ite = 0

if (f(x1)*f(x2))>0:
    print("Wrong initial guess")
else:
    while True:
        x=(x2*f(x1)-x1*f(x2))/(f(x1)-f(x2))
        ite+=1
        if f(x)==0 or abs(f(x))<e:
            print(f"Root is {x} after {ite} iterations")
            break
        if (f(x1)*f(x))>0:
            x1=x
        else:
            x2=x
