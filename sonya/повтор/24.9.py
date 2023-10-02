file = open('24.9.txt').readline()
file = file.split('XZZY')
maxx = 0
for i in file:
    maxx = max(maxx, len(i))
print(maxx + 6)
