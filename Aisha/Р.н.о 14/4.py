s = 125 + 25 ** 3 + 5 ** 9
count = 0
while s != 0:
    if s % 5 == 0:
        count += 1
    s //= 5
print(count)