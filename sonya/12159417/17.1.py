file = open('17.txt')

count = 0
maxsumm = 0

last = 0
plast = 0

for n in file:
    n = int(n)
    if (last ** 2 == plast ** 2 + n ** 2) or (plast ** 2 == last ** 2 + n ** 2) or (n ** 2 == plast ** 2 + last ** 2):
        count += 1
        maxsumm = max(maxsumm, n + last + plast)
    plast = last
    last = n
print(count,maxsumm)