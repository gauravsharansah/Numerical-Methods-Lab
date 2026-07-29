import numpy as np

u = np.zeros((5, 5), dtype=float)
u[:, 0] = [0, 50, 60, 50, 0] #left boundary
u[:, 4] = [0, 50, 60, 50, 0] #right boundary
u[0, :] = [0, 80, 100, 80, 0] #top boundary
u[4, :] = [0, 80, 100, 80, 0] #bottom boundary

tolerance = 0.0001
error = 1
iteration = 0
max_iterations = 10000

while error > tolerance and iteration < max_iterations:
    old = u.copy()

    for i in range(1, 4):
        for j in range(1, 4):
            u[i, j] = (
                u[i-1, j] +      
                u[i+1, j] +     
                u[i, j-1] +     
                u[i, j+1]      
            ) / 4

    error = np.max(np.abs(u - old))
    iteration += 1

print("Final Grid:")
print(np.round(u, 2))

print("\nInterior Values:")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"U{i},{j} = {u[i,j]:.2f}")
print("\nIterations =", iteration)
print(f"Final Error = {error:.5f}")
