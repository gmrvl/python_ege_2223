def f(n):
    if n == 1:
        return 1
    elif n > 1:
        return f(n - 1) + 2**(n - 1)
print(f(10))