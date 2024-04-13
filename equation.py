def solve_quadratic(a, b, c):
    D = b ** 2 - 4 * a * c
    if a == 0:
        return None
    if D > 0:
        x1 = (-b + D ** 0.5) / (2 * a)
        x2 = (-b - D ** 0.5) / (2 * a)
        return (x1, x2)
    elif D == 0:
        x = -b / (2 * a)
        return (x)
    else:
        return None