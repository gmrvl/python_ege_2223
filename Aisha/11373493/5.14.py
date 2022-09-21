s = 9 ** 12 + 3 ** 8 - 3
count = 0
while s != 0:
    if s % 3 == 2:
        count += 1
    s //= 3
print(count)