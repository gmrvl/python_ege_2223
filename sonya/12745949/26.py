file = open('26_demo.txt')
S, n = map(int, file.readline().split())
files = [int(i) for i in file]
files = sorted(files)
polzovateli = 0
s = 0
for i in range(n):
    if s + files[i] <= S:
        polzovateli += 1
        s += files[i]
s = s - files[polzovateli - 1]
maxx = 0
for i in range(polzovateli, len(files)):
    if (s + files[i]) <= S:
        maxx = files[i]
print(polzovateli, maxx)




