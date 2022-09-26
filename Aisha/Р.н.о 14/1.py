s = 49 **7 + 7 **21 -7
count = 0
while s != 0:
    if s % 7 == 6:
        count += 1
    s //= 7
print(count)