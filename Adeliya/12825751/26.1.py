file=open('26.1.txt')
n=int(file.readline())
summ = 0
n50 = []

for i in file:
    i = int(i)
    if i <= 50:
        summ += i
    else:
        n50.append(i)

n50 = sorted(n50)
for i in range(len(n50)):
    if i < (len(n50) // 2):
        summ += (n50[i] * 0.75)
        maxx = n50[i]
    else:
        summ += n50[i]

print(summ, maxx)