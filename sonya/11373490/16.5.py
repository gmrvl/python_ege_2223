def F(n):
    if  n == 0:
        return 0
    elif n > 0 and n % 3 == 0:
        return (F(n / 3))
    elif n % 3 > 0:
        return (n % 3 + F(n - (n % 3)))

for n in range (0,1000):
    if F(n)==9:
        print(n)

