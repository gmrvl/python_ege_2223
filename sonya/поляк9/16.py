def f(n):
    if n == 0:
        return 8
    if n > 0 and n % 3 == 0:
        return 5 + f(n / 3)
    else:
        return f(n // 3)
count = 0
for n in range(1, 100000000 + 1):
    if f(n) == 18:
        count += 1
print(count)