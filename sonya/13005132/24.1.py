file = open('24.1.txt').readline()
file = file.split('XZZY')
maxcount = 0
for i in file:
    maxcount = max(maxcount, len(i))
print(maxcount + 6)