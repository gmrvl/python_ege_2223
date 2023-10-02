file = open('26.9.txt')
N = int(file.readline())
n = [int(i) for i in file]
n = sorted(n, reverse=True)
count = [n[0]]
for i in n[1:]:
    if count[-1] - i >= 3:
        count.append(i)
print(len(count), min(count))