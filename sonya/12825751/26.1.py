file = open('26.1.txt')
n = int(file.readline())
summ = 0
maxx = 0
bolshe50 = []

for i in file:
    i = int(i)
    if i <= 50:
        summ += i
    else:
        bolshe50.append(i)

bolshe50 = sorted(bolshe50)
for i in range(len(bolshe50)):
    if i < (len(bolshe50) // 2):
        summ += (bolshe50[i] * 0.75)
        maxx = bolshe50[i]
    else:
        summ += bolshe50[i]

print(round(summ), maxx)