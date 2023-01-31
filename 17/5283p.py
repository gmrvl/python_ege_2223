file = open('5283p.txt')
M = 10000
for i in file:
    i = int(i)
    if (i % 43 == 0) and (i < M):
        M = i
print(M)
m0 = M % 10

file = open('5283p.txt')
count = 0
# a = [int(i) for i in file]

last = int(file.readline())
maxx = last

for i in file:
    i = int(i)
    if ((i + last) % M == 0) or ((i % 10) == m0) or ((last % 10) == m0):
        count += 1
        maxx = max(maxx, i, last)
print(count, maxx)

# for i in range(0, len(a) - 1):
#     for j in range(i + 1, len(a)):
#         if ((a[i] + a[j]) % M == 0) or ((a[i] % 10 == m0) or (a[j] % 10 == m0)):
#             count += 1
#             maxx = max(maxx, a[i], a[j])

