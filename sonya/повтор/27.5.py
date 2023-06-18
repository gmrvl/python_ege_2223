file = open('5-27991_B.txt')
N = int(file.readline())
maxch = 0
maxnch = 0
maxch17 = 0
maxnch17 = 0
for i in file:
    i = int(i)
    if i % 2 == 0 and i % 17 == 0:
        maxch17 = max(maxch, i)
    elif i % 2 == 1 and i % 17 == 0:
        maxnch17 = max(maxnch, i)
    elif i % 2 == 1:
        maxnch = max(maxnch, i)
    elif i % 2 == 0:
        maxch = max(maxch, i)
if maxch + maxch17 == max(maxch+maxch17, maxnch + maxnch17):
    print(maxch , maxch17)
else:
    print(maxnch , maxnch17)