file = open('24.2.txt').read()
data = file.split('A')
maxcount = 0
for i in range(len(data) - 1):
    if len(data[i]) + len(data[i+1]) > maxcount:
        maxcount = len(data[i]) + len(data[i+1])
print(maxcount + 1)


