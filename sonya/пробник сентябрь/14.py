s = 343**5 + 343**4 + 49**6 - 7**13 - 21

a = ''
while s > 0:
    a = str(int(s) % 7) + a
    s //= 7


print(a)