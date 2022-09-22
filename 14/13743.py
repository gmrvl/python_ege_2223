a = 49 ** 10 + 7 ** 30 - 49

count = 0

while a > 0:
    if a % 7 == 6:
        count += 1
    a //= 7

print(count)
