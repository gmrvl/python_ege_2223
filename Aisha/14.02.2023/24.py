file = open("24.txt")
string = file.read()
string = string.replace('AB', 'x')
string = string.replace('CB', 'x')


count = 0
maxCount = 0

for i in range(len(string)):
    if string[i] == 'x':
        count += 1
    else:
        maxCount = max(maxCount, count)
        count = 0
print(maxCount)
