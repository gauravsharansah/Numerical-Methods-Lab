import math
def simpsons_rule(f, a, b, n):
    h = (b - a) / n
    integral = (f(a) + f(b))

    for i in range(1, n):
        x_i = a + (i * h)
        if i % 2 == 0:
            integral += 2 * f(x_i)
        else:
            integral += 4 * f(x_i)

    integral *= h / 3
    return integral

def main():
    expression = input("Enter the function to integrate (use 'x' as the variable): ")
    def f(x):
        return eval(expression)
    # Set the limits of integration and number of subintervals
    a = float(input("Enter the lower limit of integration (a): "))
    b = float(input("Enter the upper limit of integration (b): "))
    n = int(input("Enter the number of subintervals (n): "))

    result = simpsons_rule(f, a, b, n)
    print(f"The integral of {expression} from {a} to {b} is approximately: {result}")

if __name__ == "__main__":
    main()
    