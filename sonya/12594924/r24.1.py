file = open('r24.1.txt').read()
count = 0
macount = 0
last = ''
for char in file:
    if char == last:
        macount = max(macount, count)
        count = 1
    else:
        count += 1
    last = char
print(macount)
