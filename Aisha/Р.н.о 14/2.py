s = 729 ** 6 + 3 ** 14 - 36
count = 0
while s != 0:
    if s % 9 == 0:
        count += 1
    s //= 9
print(count)