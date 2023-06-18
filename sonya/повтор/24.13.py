file = open('24.13.txt').read()
maxcount = count = k = 0
for char in file:
    if char == 'A':
        if k >= 3:
            maxcount = max(maxcount, count)
        count = 0
    elif char == 'E':
        k += 1
        count += 1
    else:
        count +=1
print(maxcount)