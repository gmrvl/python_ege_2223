file = open('24.txt').read()
count = 0
maxcount = 0
last = ''
for char in file:
    if len(last) < 2:
        last += char
    if len(last) == 2:
        if last == 'AE' or last == 'AN':
            count += 1
            last = ''
        else:
            maxcount = max(maxcount, count)
            count = 0
            last = last[1:] + char
print(maxcount)

