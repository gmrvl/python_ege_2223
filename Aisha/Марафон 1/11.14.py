s = 7 * 512 **120 - 6 * 64 ** 100 + 8 ** 210 - 255
count = 0
while s != 0:
    if s % 8 == 0:
        count += 1
    s //= 8
print(count)
