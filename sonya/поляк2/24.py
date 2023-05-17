from fnmatch import *
file = open('24-230.txt').readline()
file = file.split('ZZ')
a = []
for string in file:
    if fnmatch(string, '8???54???22'):
        a.append(int(string))
x = max(a)
proizved = 1
while x > 0:
    if (x % 10) % 2 == 1:
        proizved *= x % 10
    x //= 10
print(proizved)


