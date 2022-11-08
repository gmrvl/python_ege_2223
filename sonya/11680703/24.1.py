file = open('24.1.txt')

count = 0
for string in file:
    if string.count('E') > string.count('A'):
        count += 1
print(count)