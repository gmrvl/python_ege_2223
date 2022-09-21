s = 9 ** 8 + 3 ** 8 - 2
count = 2
while s != 0:
    if s % 3 == 2:
        count += 1
    s //= 3
print(count)