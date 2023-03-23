file = open('рно26.txt')
S,n = map(int, file.readline().split())
mass = [int(i) for i in file]
mass = sorted(mass)
count = 0
s = 0
for i in mass:
    if (s + i) <= S:
        s += i
        count += 1
maxx = 0
for i in range(count, len(mass)):
    if (s - mass[count - 1]) + mass[i] <= S:
        maxx = mass[i]
print(count, maxx)