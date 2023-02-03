a=49**8 + 7**24 - 7
count=0
while a!=0:
    if a % 7 == 0:
        count += 1
    a //= 7

print(count)
