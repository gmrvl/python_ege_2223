file=open('27_A.txt')
n=int(file.readline())

a = []
for i in file:
    a.append(int(i)*3)
min_sum = 1000000 ** 10
for i in range(0,n):



