def f(n):
    if n == 1:
        return 1
    elif n > 1:
        return 2*f(n-1) +1

print(f(6))