line = open().readline()

counts = [0] * 26
alth = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in range(len(line) - 2):
    if line[i] == line[i+2]:
        counts[alth.find(line[i+1])] += 1

for i in range(26):
    print(counts[i], alth[i])
print(max(counts))

