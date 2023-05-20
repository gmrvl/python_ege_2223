file = open('17-335.txt')

M = 10000
for n in file:
    n = int(n)
    if n % 43 == 0:
        M = min(M, n)

file = open('17-335.txt')
maxx = 0
count = 0
last = int(file.readline())
for n in file:
    n = int(n)
    if (((n + last) % M == 0) and not((str(last)[-1] == str(M)[-1]) or (str(n)[-1] == str(M)[-1]))) or (not((n + last) % M == 0) and ((str(last)[-1] == str(M)[-1]) or (str(n)[-1] == str(M)[-1])))  :
        count += 1
        maxx = max(maxx, n, last)
    last = n
print(maxx, count)
