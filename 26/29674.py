file = open('29674.txt')
n = int(file.readline())
products = []
summ = 0
for i in file:
    pr = int(i)
    if pr <= 50:
        summ += pr
    else:
        products.append(pr)
products = sorted(products)
disc = 0
n = len(products)
for i in range(n):
    if i < n//2:
        disc += products[i] * 0.75
    else:
        summ += products[i]
summ += int(disc) + 1
print(summ, products[n//2 - 1])

