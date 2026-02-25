def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    x = x0
    f = a * x ** 2 + b * x + c
    f_dx = 2*a*x + b
    x_min = -b / 2*a
    for _ in range(steps):
        f_dx = 2*a*x + b
        x = x - lr * f_dx
        f = a * x ** 2 + b * x + c
        if abs(x - x_min) < 0.0001:
            break
    return x