file = open('24.2.txt').read()
count = 0
maxcount = 0
last = ''
for i in file:
    if i == last:
        maxcount = max(maxcount, count)
        count = 1
    else:
        count += 1
    last = i
print(maxcount)
