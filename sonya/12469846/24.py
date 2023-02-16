file = open('zadanie24_2.txt').read()

count = 0
maxcount = 0


for char in file:
    if char == 'L':
        count += 1
    else:
        maxcount = max(maxcount, count)
        count = 0
maxcount = max(maxcount, count)
print(maxcount)