def f(n):
    if n == 0:
        return 0
    elif n % 2 == 1:
        return f(n - 1) + 1
    else:
        return f(n / 2)


count = 0
for n in range(1_000):
    if f(n) == 3:
        count += 1
        print(n)
print(count)
