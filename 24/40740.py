file = open('40740.txt').read()
maxx = 0
data = file.split('A')
for i in data:
    if i.count('E') >= 3 and len(i) > maxx:
        maxx = len(i)
print(maxx)
