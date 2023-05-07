file = open('6759.txt')

n = int(file.readline())
a = []

for i in file:
    a.append(int(i))

a = sorted(a)
summ = 0
want_cost = 0
real_cost = 0

for i in range(n//3*2+1):
    want_cost += a[i]

for i in range(0, n, 3): # подумать какие товары берутся 
    real_cost += a[i]
for i in a:
    summ += i
print(n)
print(want_cost, summ - real_cost)
