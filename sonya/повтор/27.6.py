file = open('6-28130_B.txt')
N = int(file.readline())
n = [int(i) for i in file]
i = 0
k = 0
while i != N:
    for x in range(i + 1, N):
        if (n[i] + n[x]) % 80 == 0 and (n[i] > 50 or n[x] > 50):
            k += 1
    i += 1
print(k)