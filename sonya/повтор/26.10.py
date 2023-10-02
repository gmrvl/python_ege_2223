file = open('26.10.txt')
N = int(file.readline())
n = [['0'] * 10001 for i in range(10001)]
for i in file:
    r, m = map(int, i.split())
    n[r][m] = '1'
maxcount = 0
ryad = 0
for i in range(1, 10001):
    count = 0
    for j in range(1,10001):
        if j % 2 != 0:
            if n[i][j] == '1' and n[i][j+1] == '0':
                count += 1
            else:
                if maxcount < count:
                    maxcount = count
                    ryad = i
                count = 0
print(maxcount, ryad)