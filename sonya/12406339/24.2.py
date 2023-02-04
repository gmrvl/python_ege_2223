file = open('zadanie24_1 (2).txt').read()

count = 0
maxcount = 0

for char in file:
    if char == 'A':
        count +=1
    else:
        maxcount = max(maxcount, count)
        count = 0
print(maxcount)