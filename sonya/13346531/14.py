s = 4 ** 36 + 3 * (4 ** 20) + 4 **15 + 2 * (4** 7) + 49

s16 = ''
while s > 0:
    s16 = str(s % 16) + s16
    s //= 16
print(s16)