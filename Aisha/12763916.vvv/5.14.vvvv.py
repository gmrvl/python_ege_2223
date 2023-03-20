s = (49 ** 8) + (7 ** 24) - 7

count = 0
while s > 0:
    if s % 7 == 0:
        count += 1
    s //= 7

print(count)