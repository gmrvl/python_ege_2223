# 1 1 1
# 0 0 0
# 0 1 2

file = open('27-A.txt')
n = int(file.readline())


min2 = 100**10

min0 = []
min1 = []

for i in file:
    i = int(i)
    if i % 3 == 0:
        min0.append(i)
    elif i % 3 == 1:
        min1.append(i)
    else:
        min2 = min(min2, i)

min0 = sorted(min0)
min1 = sorted(min1)
min01 = min0[0]
min02 = min0[1]
min03 = min0[2]
min11 = min1[0]
min12 = min1[1]
min13 = min1[2]


print(min(min01 + min02 + min03, min11 + min12 + min13, min01 + min11 + min2))