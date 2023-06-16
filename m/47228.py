file = open('24 (13).txt').readline()
count = 0
max_count = 0
g = ['A', 'O']
s = ['B', 'C', 'D']
for i in range(0, len(file) - 1):
    if (file[i] in g and file[i + 1] in s) or (file[i] in s and file[i + 1] in g):
        count += 1
    else:
        max_count = max(count, max_count)
        count = 1
print(max_count)
