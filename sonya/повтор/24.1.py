file = open('24').read()
count = 0
maxcount = 0
last = ''
for char in file:
    if last != char:
        count += 1
    else:
        maxcount = max(maxcount, count)
        count = 1
    last = char
print(maxcount)