def f(n):
    if n == 1:
        1
    return f(n - 1) + f(n - 2)