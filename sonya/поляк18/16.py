def f(n):
    if n < 2:
        return n
    elif n % 2 == 0:
        return f(n / 2) + 1
    else:
        return f(3*n + 1) + 1


count = 0
for i in range(1, 100000):
    if f(i) == 16:
        count += 1
print(count)