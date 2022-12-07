s = 25**6 + 5**18 - 5

count = 0

while s > 0:
    if s % 5 == 4:
        count += 1
    s //= 5
print(count)