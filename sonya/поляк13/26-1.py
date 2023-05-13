file = open('26-94.txt')
n, k = map(int, file.readline().split())

floor_1 = [[0] * k for i in range(n)]
floor_2 = [[0] * k for j in range(n)]
for i in file:
    floor, ryad, mesto = map(int, i.split())
    if floor == 1:
        floor_1[ryad][mesto - 1] = 1
    else:
        floor_2[ryad][mesto - 1] = 1

count, max_ryad = 0, 0
c = 0
for i in floor_1:
    if i != [0, 0, 0, 0, 0, 0]:
        if i[0:4] == [0, 0, 0, 0] or i[2:6] == [0, 0, 0, 0]:
            count += 1
            max_ryad = c
    c += 1

for i in range(1, len(floor_2)):
    if floor_2[i] != [0, 0, 0, 0, 0, 0]:
        if floor_2[i][0:4] == [0, 0, 0, 0] or floor_2[i][2:6] == [0, 0, 0, 0]:
            count += 1
            max_ryad = max(i, max_ryad)
print(count, max_ryad)

