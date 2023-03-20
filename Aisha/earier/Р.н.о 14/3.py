s =  9 ** 18 + 3 ** 54 -9
count = 0
while s != 0:
    if s% 3 == 2:
        count += 1
    s //= 3
print(count)