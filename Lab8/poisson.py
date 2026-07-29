import numpy as np

h = 1/3
n = round(1/h) + 1  

def f(x, y):
    return 729 * x**2 * y**2  

u = np.zeros((n, n), dtype=float)
u[0, :] = 0   # top boundary
u[-1, :] = 0  # bottom boundary
u[:, 0] = 0   # left boundary
u[:, -1] = 0  # right boundary

tolerance = 0.0001
error = 1
iteration = 0
max_iterations = 10000

while error > tolerance and iteration < max_iterations:
    old = u.copy()

    for i in range(1, n - 1):
        for j in range(1, n - 1):
            x, y = i * h, j * h
            u[i, j] = (
                u[i-1, j] +
                u[i+1, j] +
                u[i, j-1] +
                u[i, j+1] -
                h**2 * f(x, y)
            ) / 4

    error = np.max(np.abs(u - old))
    iteration += 1

print("Final Grid:")
print(np.round(u, 2))

print("\nInterior Values:")
for i in range(1, n - 1):
    for j in range(1, n - 1):
        print(f"U{i},{j} = {u[i,j]:.2f}")
print("\nIterations =", iteration)
print(f"Final Error = {error:.5f}")
