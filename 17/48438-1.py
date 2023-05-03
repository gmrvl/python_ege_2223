count = m = 0
f = open('48438.txt')
l = [int(i) for i in f]
min_sp = 0
for i in range(len(l)):
    if abs(l[i]) % 10 == 7:
        min_sp = min(min_sp, l[i])
print(min_sp)

for i in range(len(l) - 1):
    if ((abs(l[i]) % 10 == 7 and (abs(l[i + 1])) % 10 != 7) or (
            (abs(l[i])) % 10 != 7 and abs((l[i + 1])) % 10 == 7)) and ((l[i] ** 2 + l[i + 1] ** 2) < min_sp ** 2):
        count += 1
        print(l[i], l[i + 1])
        m = max(m, (l[i] ** 2 + l[i + 1] ** 2))
print(count, m)