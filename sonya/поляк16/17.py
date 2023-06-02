file = open('17-342.txt')
min37 = 10000
max73 = 0
for n in file:
    n = int(n)
    if n % 37 == 0:
        min37 = min(min37, n)
    if n % 73 == 0:
        max73 = max(max73,n)
print(min37, max73)
count = 0
minsumm = 1000000000
file = open('17-342.txt')
last = int(file.readline())
for n in file:
    n = int(n)
    if ((max73 < n < min37) and not(max73 < last < min37)) or ((max73 < last < min37) and not(max73 < n < min37)):
        count += 1
        minsumm = min(minsumm,n + last)
    last = n
print(count, minsumm)


