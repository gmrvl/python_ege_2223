s = (9 ** 8) * (3 ** 20) - (3 ** 10) - 3

count = 0
while s != 0:
    if s % 3 == 2:
        count += 1
    s //= 3
print(count)
