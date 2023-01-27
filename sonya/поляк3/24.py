#комбинаций BAC и СAB
file = open('24-224.txt').read()
count = 0
maxcount = 0
c = 0
b = 0

for char in file:
    if char == 'B' and c == 0:
        count += 1
        c = 1
        b = 0
    if char == 'B' and b == 2:
        count += 1
        c = 0
        b = 0
    if char == 'C' and c == 2:
        count += 1
        c = 0
        b = 0
    if char == 'C' and b == 0:
        count += 1
        c = 0
        b = 1
    if char == 'A' and c == 1:
        count += 1
        c = 2
        b = 0
    if char == 'A' and b == 1:
        count += 1
        c = 0
        b = 2
    else:
        maxcount = max(maxcount, count)
        count = 0
        c = 0
print(maxcount)