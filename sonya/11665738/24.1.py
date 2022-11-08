file = open('24.1.txt').read()

count = 0
maxcount = 0
с = 0

for char in file:
    if char == 'A':
        if с == 2:
            if count > maxcount:
                maxcount = count
            с = 0
            count = 0
        else:
            count += 1
        с += 1
    else:
        count += 1
print(maxcount)