file = open('24.4.txt')
count = 0
for string in file:
    if string.count('A') < string.count('E'):
        count += 1
print(count)