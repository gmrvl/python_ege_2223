file = open('24.16.txt').readline()
file = file.replace('B', 'A')
file = file.replace('C', 'A')
file = file.split('AA')
maxcount = 0
for i in file:
    maxcount = max(maxcount, len(i))
print(maxcount + 2)