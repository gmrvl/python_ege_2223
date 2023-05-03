from fnmatch import *

file = open('24-228.txt').readline()
file = file.split('X')

ns = []
for string in file:
    if len(string) == 11:
        if fnmatch(string, '3????78??45'):
            ns.append(int(string))
maxx = max(ns)
print(maxx)
summnch = 0
proizvch = 1
for i in range(0, len(str(maxx))):
    maxx = str(maxx)
    if int(maxx[i]) % 2 == 0:
        proizvch *= int(maxx[i])
    else:
        summnch += int(maxx[i])
print(summnch + proizvch)

