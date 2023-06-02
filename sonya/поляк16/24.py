from fnmatch import*
file = open('24-228.txt').readline()
file = file.split('SS')
n = []
for string in file:
    if fnmatch(string, '12????77??9'):
        n.append(int(string))
print(max(n))