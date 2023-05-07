file = open('р26.1.txt')

n = int(file.readline())

boxes = [int(i) for i in file]
boxes = sorted(boxes, reverse=True)
box = []
box.append(boxes[0])
for i in range(1, n):
    if box[-1] - boxes[i] >= 3:
        box.append(boxes[i])
print(len(box), box[-1])