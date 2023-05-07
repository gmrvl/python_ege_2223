file = open('47230.txt')
n = file.readline()
kor = []
for i in file:
    kor.append(int(i))

kor = sorted(kor, reverse=True)
pod = [kor[0]]
for i in range(1, len(kor)):
    if pod[-1] - kor[i] >= 3:
        pod.append(kor[i])
print(pod[-1], len(pod))
