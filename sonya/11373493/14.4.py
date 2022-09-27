s = 729**8 - 3**18 + 85

count = 0
while s>0:
    if s % 9 == 0:
        count += 1
    s //= 9
print(count)