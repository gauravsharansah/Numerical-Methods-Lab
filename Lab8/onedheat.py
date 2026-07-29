import numpy as np

h, k = 0.2, 0.02
nx = round(1/h) + 1    # space points: x = 0, 0.2, ..., 1
nt = round(0.1/k) + 1  # time steps:   t = 0, 0.02, ..., 0.1

x = np.linspace(0, 1, nx)
def f(x):
    return np.sin(np.pi * x)  # initial condition u(x, 0)

u = np.zeros((nt, nx), dtype=float)
u[0, :] = f(x)   # initial condition (t=0 row)
u[:, 0] = 0      # left boundary  (x=0)
u[:, -1] = 0     # right boundary (x=1)

r = k / (h**2)
print(f"r = k/h^2 = {r}")  # should be 0.5 for this explicit (Bender-Schmidt) scheme

for i in range(1, nt):
    for j in range(1, nx - 1):
        u[i, j] = (u[i-1, j-1] + u[i-1, j+1]) / 2

print("Final Grid (rows = time, cols = space):")
print(np.round(u, 4))

print("\nValues:")
for i in range(nt):
    for j in range(nx):
        print(f"u[t={i*k:.2f}][x={j*h:.2f}] = {u[i,j]:.4f}")
        