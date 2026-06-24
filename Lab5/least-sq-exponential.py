import numpy as np
def leastsq(n,x,y):
    log_y = np.log(y)
    sum_x = np.sum(x)
    sum_log_y = np.sum(log_y)
    sum_x_log_y = np.sum(x * log_y)
    sum_x2 = np.sum(x * x)
    b = ((n * sum_x_log_y) - (sum_x * sum_log_y)) / ((n * sum_x2) - (sum_x**2))
    log_a = (sum_log_y - (b * sum_x)) / n
    a = np.exp(log_a)
    print(f"The required equation is: y = {a:.3f} * e^({b:.3f}x)")

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

    leastsq(n,x,y)


if __name__ == "__main__":
    main()