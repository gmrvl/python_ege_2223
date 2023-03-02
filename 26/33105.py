file = open('33105.txt')

n = file.readline()
summ = 0
s = []
for i in file:
    i = int(i)
    if i > 100:
        s.append(i)
    else:
        summ += i
s = sorted(s)
maxx = 0
for i in range(len(s)):
    if i < len(s) // 2:
        summ += s[i] * 0.70
        maxx = s[i]
    else:
        summ += s[i]
print(round(summ), maxx)

