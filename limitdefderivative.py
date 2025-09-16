import numpy as np
import matplotlib.pyplot as plt
import math

# -----------------------------
# 1. Limit definition of derivative
# -----------------------------
def limit_derivative(f, x, h):
    return (f(x + h) - f(x)) / h

# -----------------------------
# 2. Predefined functions
# -----------------------------
def f1(x):
    return math.sin(x)

def f2(x):
    return x**4

def f3(x):
    return x**2 * math.log(x)

# -----------------------------
# 2. Evaluate derivative of f3 at x=1 with different h
# -----------------------------
h_values = [2, 0.1, 0.00001]
for h in h_values:
    deriv = limit_derivative(f3, 1, h)
    print(f"Derivative of f3 at x=1 with h={h}: {deriv}")

# -----------------------------
# 5. Plot approximate derivatives
# -----------------------------
def plot_approx_deriv(f):
    x_vals = np.linspace(0.1, 2, 100)  # avoid log(0)
    h_vals = [0.5, 0.1, 0.01, 0.001]
    
    plt.figure(figsize=(8,5))
    
    for h in h_vals:
        deriv_vals = [limit_derivative(f, x, h) for x in x_vals]
        plt.plot(x_vals, deriv_vals, label=f"h={h}")
    
    # True derivative curve
    if f == f1:
        y_vals = [math.cos(x) for x in x_vals]
        plt.plot(x_vals, y_vals, 'k--', label="True derivative cos(x)")
    elif f == f2:
        y_vals = [4*x**3 for x in x_vals]
        plt.plot(x_vals, y_vals, 'k--', label="True derivative 4x^3")
    elif f == f3:
        y_vals = [2*x*math.log(x) + x for x in x_vals]  # derivative of x^2*ln(x)
        plt.plot(x_vals, y_vals, 'k--', label="True derivative 2x ln(x) + x")
    
    plt.title("Limit Definition Approximate Derivative")
    plt.xlabel("x")
    plt.ylabel("f'(x)")
    plt.legend()
    plt.show()

# -----------------------------
# 6. Graph derivatives of f1
# -----------------------------
plot_approx_deriv(f1)

# -----------------------------
# 9. Graph derivatives of f2
# -----------------------------
plot_approx_deriv(f2)

# -----------------------------
# Optional: Graph derivatives of f3
# -----------------------------
plot_approx_deriv(f3)
