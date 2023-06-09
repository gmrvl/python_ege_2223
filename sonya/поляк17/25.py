from fnmatch import*
count = 0
for n in range(73, 10**10, 73):
    if fnmatch(str(n), '12345*76'):
            count += 1
            print(n, n // 73)
            if count == 5:
                break