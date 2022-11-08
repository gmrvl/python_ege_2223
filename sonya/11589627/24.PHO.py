file = open('24.txt').read()

count = 0
maxcount = 0
last = ''

for char in file:
    if last == 'P' and char == 'P':
        if count > maxcount:
            maxcount = count
        count = 1
    else:
        count += 1
    last = char
print(maxcount)