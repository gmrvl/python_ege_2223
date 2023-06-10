file = open('26-92.txt')
k = file.readline()
n = []
for i in file:
    ryad, mesto, z = i.split()
    n.append([int(ryad), int(mesto), z])
n = sorted(n)
# print(n)
maxcount = 0
nomer = 0
count = 0
for i in range(1, len(n)):
    if (n[i][0] == n[i-1][0]) and (n[i][1] == (n[i-1][1] + 1)) and (n[i][2] == n[i-1][2] == '+'):
        count += 1
    else:
        maxcount = max(maxcount, count)
        if n[i][2] == '+':
            count = 1
        else:
            count = 0
print(maxcount, nomer)
