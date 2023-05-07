s = 125**4 + 25**8 - 30
count = 0
while s > 0:
    if s % 5 == 4:
        count += 1
    s //= 5
print(count)