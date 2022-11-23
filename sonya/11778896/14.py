s = 6*(343**5) + 5*(49**7) - 50

count = 0
while s > 0:
    if s % 7 == 6:
        count += 1
    s //= 7
print(count)