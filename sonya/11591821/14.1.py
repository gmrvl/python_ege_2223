s = 9**7 + 3**21 - 9

count = 0
while s > 0:
    if s%3 == 2:
        count += 1
    s //= 3
print(count)