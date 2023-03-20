s = 36**7 + 6**19 - 18

count = 0
while s != 0:
    if s % 6 == 5:
        count += 1
    s //= 6
print(count)
