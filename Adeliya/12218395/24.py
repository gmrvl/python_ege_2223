file = open('24.txt').read()

last = ''
maxcount = 0
c = 0
for i in file:
    if i == 'A':
        if c == 1:
            if len(last) > maxcount:
                maxcount = len(last)
            last = last[last.find('A')+1:] + 'A'
            # print(last)
        else:
            last += i
            c += 1
    else:
        last += i
if len(last) > maxcount:
    maxcount = len(last)
print(maxcount)
