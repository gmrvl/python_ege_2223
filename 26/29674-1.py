file = open('29674.txt')
n = file.readline()
products = []
summ = 0

for i in file:
    i = int(i)
    if i <= 50:
        summ += i
    else:
        products.append(i)

products = sorted(products)

m = len(products) // 2
for i in range(0, len(products)):
    if i < m:
        summ += products[i] * 0.75
    else:
        summ += products[i]

print(summ)
