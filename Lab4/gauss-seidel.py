import numpy as np

def reorder_for_dominance(A, b):
    A, b = np.array(A, float), np.array(b, float)
    n = len(b)
    rows_left = list(range(n))
    order = []

    for col in range(n):
        best_row = max(rows_left, key=lambda r: abs(A[r, col]))
        order.append(best_row)
        rows_left.remove(best_row)

    return A[order], b[order]


def is_diagonally_dominant(A):
    n = len(A)
    return all(abs(A[i, i]) > sum(abs(A[i])) - abs(A[i, i]) for i in range(n))


def gauss_seidel(A, b, tol=1e-10, max_iter=1000):
    A, b = np.array(A, float), np.array(b, float)
    n = len(b)
    x = np.zeros(n)

    for iteration in range(1, max_iter + 1):
        x_old = x.copy()
        for i in range(n):
            s = np.dot(A[i], x) - A[i, i] * x[i]
            x[i] = (b[i] - s) / A[i, i]
        if np.linalg.norm(x - x_old, np.inf) < tol:
            return x, iteration

    raise ValueError("Did not converge within max_iter iterations.")


def main():
    n = int(input("Enter number of variables: "))
    A, b = [], []

    for i in range(n):
        prompt = f"Row {i + 1} ({n} coefficients + RHS): "
        row = list(map(float, input(prompt).split()))
        A.append(row[:n])
        b.append(row[n])

    A, b = reorder_for_dominance(A, b)

    print(f"\nReordered coefficient matrix A:\n{A}")
    print(f"Reordered RHS vector b (column form):\n{b.reshape(-1, 1)}")

    if not is_diagonally_dominant(A):
        print("\nWarning: no row ordering makes this matrix diagonally dominant. Gauss-Seidel may not converge.\n")
    else:
        print("Matrix is diagonally dominant after reordering.\n")

    x, iterations = gauss_seidel(A, b)
    print(f"Converged in {iterations} iterations.")
    print(f"Solution: {x}")

if __name__ == "__main__":
    main()