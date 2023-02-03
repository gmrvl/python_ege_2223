file=open('24.txt').read()
last = ''
maxcount = 0
c = 0
for i in file:
    if i == 'D':
        if c == 1:
            if len(last) > maxcount:
                maxcount = len(last)
            last = last[last.find('D')+1:] + 'D'
        else:
            last += i
            c += 1
    else:
        last += i
if len(last) > maxcount:
    maxcount = len(last)
print(maxcount)