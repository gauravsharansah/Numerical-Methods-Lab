import numpy as np
def lagrange(n,x,y,Xp):
    Yp = 0
    for i in range (n):
        ratio = 1
        for j in range (n):
            if(i!=j):
                ratio *= (Xp-x[j])/(x[i]-x[j])
        Yp += ratio * y[i]
    print(f"The value of y is: {Yp}")

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

    Xp = int(input("Enter value of x for which y is needed: "))

    lagrange(n,x,y,Xp)


if __name__ == "__main__":
    main()