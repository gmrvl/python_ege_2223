file = open('6757.txt')

count = 0
maxCount = 0
last = ''

n = file.readline().replace('CFE', 'X')
n = n.replace('FCE', 'X')
print(n)
for char in n:
    if char == 'X':
        count += 1
    else:
        if count > maxCount:
            maxCount = count
        count = 0
print(maxCount)