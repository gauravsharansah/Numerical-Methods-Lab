import math
def simpsons_rule(f, a, b, n):
    if n % 3 != 0:
        print("Number of subintervals (n) must be divisible by 3 for Simpson's rule.")
        return
    h = (b - a) / n
    integral = (f(a) + f(b))

    for i in range(1, n):
        x_i = a + (i * h)
        if i % 3 == 0:
            integral += 2 * f(x_i)
        else:
            integral += 3 * f(x_i)

    integral *= 3*h / 8
    
    print(f"The integral from {a} to {b} is approximately: {integral}")

def main():
    expression = input("Enter the function to integrate (use 'x' as the variable): ")
    def f(x):
        return eval(expression)
    # Set the limits of integration and number of subintervals
    a = float(input("Enter the lower limit of integration (a): "))
    b = float(input("Enter the upper limit of integration (b): "))
    n = int(input("Enter the number of subintervals (n): "))

    simpsons_rule(f, a, b, n)

if __name__ == "__main__":
    main()
    