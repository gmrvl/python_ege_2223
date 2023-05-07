file = open('24 (4).txt').read()
count = 0
maxcount = 0
last = ''
s = ''
max_s = ''
for char in file:
    if char == 'L':
        if last == 'K':
            if count > maxcount:
                maxcount = count
                max_s = s
            # maxcount = max(maxcount, count)
            count = 1
            s = char
        else:
            count += 1
            s += char
    if char == 'K':
        if last == 'L':
            if count > maxcount:
                maxcount = count
                max_s = s
            count = 1
            s = char
        else:
            count += 1
            s += char
    else:
        count += 1
        s += char
    last = char
maxcount = max(maxcount, count)
print(maxcount, max_s)
