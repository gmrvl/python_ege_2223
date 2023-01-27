maxdell = 0
maxdellDigit = 0
for n in range(568023, 569231):
    sq = int(n ** 0.5)
    count = 0
    for i in range(1, sq):
        if n % i == 0:
            count += 2
    if n ** 0.5 == sq:
        count += 1
    if count > maxdell:
        maxdell = count
        maxdellDigit = n
print(maxdell, maxdellDigit)

