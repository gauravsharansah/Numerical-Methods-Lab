import math
def f(x):
    return eval(expression)

expression = input("Enter function in terms of x: ")
a = float(input("Enter lower limit: "))
b = float(input("Enter upper limit: "))
n = int(input("Enter number of subintervals (multiple of 4): "))

if n % 4 != 0:
    print("Error: Number of subintervals must be a multiple of 4 for Boole's Rule.")
else:
    h = (b - a) / n
    total = 7 * (f(a) + f(b))
    
    for i in range(1, n):
        if i % 4 == 0:
            total += 14 * f(a + i * h)
        elif i % 2 == 0:
            total += 12 * f(a + i * h)
        else:
            total += 32 * f(a + i * h)

    result = (2 * h / 45) * total

    print("Approximate integral =", result)
    