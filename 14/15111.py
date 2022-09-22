s = 25 ** 5 + 5 ** 14 - 5

count = 0
while s != 0:
    if s % 5 == 4:
        count += 1
    s //= 5

print(count)
