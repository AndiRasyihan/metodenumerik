import math

def regula_falsi_illinois(f, a, b, tol=1e-8, maxiter=10000, verbose=False):
    fa = f(a); fb = f(b)
    if fa == 0: return a, 0.0, 0, [(0,a,fa)]
    if fb == 0: return b, 0.0, 0, [(0,b,fb)]
    if fa * fb > 0:
        raise ValueError("f(a) and f(b) must have opposite signs (bracket).")
    iter_data = []
    last_changed = None
    for k in range(1, maxiter+1):
        c = (a*fb - b*fa) / (fb - fa)
        fc = f(c)
        iter_data.append((k, a, b, c, fa, fb, fc))
        if verbose:
            print(f"Iter {k:3d}: a={a:.12f}, b={b:.12f}, c={c:.12f}, f(c)={fc:.12e}")
        if abs(fc) < tol:
            return c, fc, k, iter_data
        if fa * fc < 0:
            # root in [a,c] => replace b
            b, fb = c, fc
            if last_changed == "b":
                fa *= 0.5
            last_changed = "b"
        else:
            # root in [c,b] => replace a
            a, fa = c, fc
            if last_changed == "a":
                fb *= 0.5
            last_changed = "a"
        if abs(b - a) < 1e-16:
            break
    return c, f(c), k, iter_data

def f(x):
    return x**3 - 2*x**2 + 3*x - 5

a = -2.0
b = 2.0

root, froot, iterations, history = regula_falsi_illinois(f, a, b, tol=1e-8, maxiter=10000, verbose=False)

print("Result for f(x)=x^3 - 2x^2 + 3x - 5 with bracket [-2, 2]:")
print(f"Root estimate c = {root:.12f}")
print(f"f(c) = {froot:.12e}")
print(f"Iterations = {iterations}\n")

# print last up to 12 iterations
print("Last iterations: (k, a, b, c, f(a), f(b), f(c))")
for row in history[-12:]:
    k,a,b,c,fa,fb,fc = row
    print(f"{k:3d} | {a:.12f} | {b:.12f} | {c:.12f} | {fa:.3e} | {fb:.3e} | {fc:.3e}")
