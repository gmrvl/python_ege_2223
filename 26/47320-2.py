file = open('47230.txt')
n = file.readline()
box = []

for i in file:
    box.append(int(i))

box = sorted(box, reverse=True)

present = [box[0]]
for i in range(1, len(box)):
    if present[-1] - box[i] >= 3:
        present.append(box[i])

print(present[-1], len(present))