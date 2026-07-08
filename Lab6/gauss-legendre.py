import math
def f(x):
    return eval(expression)

expression = input("Enter function in terms of x: ")

a = float(input("Enter lower limit: "))
b = float(input("Enter upper limit: "))
u1 = 1/math.sqrt(3)
u2 = -u1
w1 = 1
w2 = 1

t1 = ((b - a) / 2) * u1 + ((b + a) / 2)
t2 = ((b - a) / 2) * u2 + ((b + a) /2)

result = (w1 * f(t1) + w2 * f(t2))*((b - a) / 2)
print("Approximate integral =", result)
