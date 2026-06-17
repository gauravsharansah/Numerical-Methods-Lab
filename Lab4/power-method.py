import numpy as np

def power_method(A, x0, tol=1e-8, max_iter=1000):
    A = np.array(A, float)
    x = np.array(x0, float)
    x = x / np.linalg.norm(x, np.inf)  # normalize so largest entry has magnitude 1

    lam_old = 0.0
    for iteration in range(1, max_iter + 1):
        y = A @ x
        idx = np.argmax(np.abs(y))
        lam_new = y[idx]         
        x_new = y / lam_new     

        if abs(lam_new - lam_old) < tol:
            return lam_new, x_new, iteration

        x = x_new
        lam_old = lam_new

    raise ValueError("Did not converge within max_iter iterations.")


def main():
    n = int(input("Enter the size of the square matrix: "))
    A = []

    print(f"\nEnter the {n} elements of each row of the matrix.")
    for i in range(n):
        row = list(map(float, input(f"Row {i + 1}: ").split()))
        A.append(row)

    x0 = [1.0] * n  # default initial guess vector

    print(f"\nMatrix A:\n{np.array(A)}")
    lam, vec, iterations = power_method(A, x0)

    print(f"\nConverged in {iterations} iterations.")
    print(f"Dominant eigenvalue: {lam:.6f}")
    print(f"Dominant eigenvector (normalized so largest entry = 1):\n{vec}")


if __name__ == "__main__":
    main()