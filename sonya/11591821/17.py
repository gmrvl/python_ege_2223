file = open('17.txt')
last = int(file.readline())
count = 0
maxsumm = 0
for string in file:
    string = int(string)
    if abs(string) % 3 == 0 or abs(last) % 3 == 0:
        count += 1
        maxsumm = max(maxsumm, last + string)
    last = string
print(count, maxsumm)