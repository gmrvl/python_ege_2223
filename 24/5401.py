file = open('5401.txt').read()
count = 0
maxcount = 0
last = ''
group = ''
strr = ''

for char in file:
    if char == 'A':
        if last == '':
            count = 0
        elif last == group:
            count += len(group)
            strr += group + 'A'
        else:
            maxcount = max(count + 1, maxcount)
            last = ''
            count = 1 + len(last)
            print(strr)
            strr = 'A'
        group = last
        last = ''
        count += 1
    else:
        last += char
print(maxcount)
