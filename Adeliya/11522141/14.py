a = 343**5 + 343**4 + 49**6 - 7**13 - 21
b=[]
for i in range(7):
    b.append(0)
while a!=0:
    b[a%7] += 1
    a//=7
print(b)

