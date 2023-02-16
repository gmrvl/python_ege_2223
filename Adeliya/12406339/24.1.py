file=open('24.1.txt').read()
count = 0
maxcount = 0
c = 0
for i in file:
    if i == 'X' and c == 0:
        count += 1
        c = 1
    elif i== 'Y' and c == 1:
        count += 1
        c = 2
    elif i == 'Z' and c == 2:
        count += 1
        c = 0
    else:
        maxcount = max(maxcount, count)
        count = 0
        c = 0
print(maxcount)


