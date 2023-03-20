s = 343 ** 5 + 343 ** 4 + 49 ** 6 - 7 ** 13 - 21
count = 0
while s != 0:
    if s % 7 == 6:
        count += 1
    s //= 7
print(count)