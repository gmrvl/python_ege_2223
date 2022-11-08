s = 343 ** 5 + 343 ** 4 + 49 ** 6 - 7 ** 13 - 21
count = 0
seven = ''
while s != 0:
    seven = str(s % 7) + seven
    s //= 7

for i in range(0, 7):
    i = str(i)
    if i in seven:
        count += 1
print(count)
