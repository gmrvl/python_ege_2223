def F(n):
    if n == 0:
        return 0
    elif n > 0 and n % 2 == 0:
        return  F(n / 2)
    elif n % 2 != 0:
        return  1 + F(n - 1)

count = 0
for n in range (1,901):
    if  F(n) == 9 :
        count = count + 1
print(count)