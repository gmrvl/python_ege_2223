f = open('37162B.txt')
k, s = 89, 0
mins = {0: (0, 0)}
res = []
n = int(f.readline())
for i in range(1, n + 1):
    s += int(f.readline())
    if s % k in mins:
        res += [(s - mins[s % k][0], i - mins[s % k][1])]
        # print([(s - mins[s % k][0], i - mins[s % k][1])])
    else:
        mins[s % k] = (s, i)
print(mins)
print(max(res)[1])
