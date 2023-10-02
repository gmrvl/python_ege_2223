k = int(input())
m = int(input())
n = int(input())

if n <= k:
    print(m * 2)
if n % k == 0:
    print((n // k) * 2 * m)
else:
    print(((n // k) + 1) * 2 * m)
